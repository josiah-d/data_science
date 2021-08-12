from scipy import stats
import numpy as np
import pandas as pd
import random
from typing import List, Optional


class Strategy(object):
    """Strategy for solving the Multi-Armed Bandit Problem."""

    def __init__(self, bandits: list, seed: Optional[int]=None) -> None:
        """
        Parameters
        ----------
        bandits: list of Bandit objects,
                  each with a pull method that returns a bool.
        seed:     int to initialize random number generator."""
        self._bandits = bandits
        self.seed = seed
        self._choices = [] # type: List[int]
        self._results = [] # type: List[bool]
        self.scores = pd.DataFrame(np.zeros((len(self._bandits), 2)),
                                   columns=['trials', 'wins'])
        # seed the random number generators so you get the same results every
        # time.
        if seed:
            np.random.seed(self.seed)
            random.seed(self.seed)

    def sample(self, n: int=1) -> None:
        """Simulate n rounds of running the bandit machine

        Parameters
        -----------
        n : int number of rounds
        """
        for k in range(n):
            choice = self.choose()
            result = self._bandits[choice].pull()
            self.update(choice, result)

    def update(self, choice: int, result: bool) -> None:
        """Update the log with a new result.

        Parameters
        ----------
        choice: int   the index of the bandit tried
        result: bool  did it pay off?
        """
        self._choices.append(choice)
        self._results.append(result)
        self.scores.loc[choice, 'trials'] += 1
        self.scores.loc[choice, 'wins'] += result

    def regret(self):
        """Return the regret over time, defined as the difference of
        the optimal expected value (if the best bandit were chosen)
        and the expected value given the choices made."""
        probabilities = np.array([bandit.p for bandit in self._bandits])
        p_opt = max(probabilities)
        return np.cumsum(p_opt -
                         probabilities[self._choices])

    def best(self) -> int:
        """Return the index of the bandit with the highest success rate.
        If any haven't been tested, return one of those at random.
        Otherwise if two are tied, return the first."""
        if self.scores.trials.min() == 0:
            return np.random.randint(0, len(self._bandits))
        return (self.scores.wins / self.scores.trials).idxmax()

    def choose(self) -> int:
        """Return the index of the selected bandit."""
        raise NotImplementedError


class RandomStrategy(Strategy):
    """Pick a bandit randomly with equal probability. """

    def choose(self) -> int:
        """Return the index of the selected bandit."""
        return np.random.randint(0, len(self._bandits))


class GreedyStrategy(Strategy):
    """Always pick the bandit with the best observed proportion of winning."""

    def choose(self) -> int:
        """Return the index of the selected bandit."""
        return self.best()


class EpsilonGreedyStrategy(Strategy):
    """
    Pick a bandit randomly with equal probability at with probability epsilon.
    Otherwise pick the bandit with the best observed proportion of winning.
    """
    def __init__(self,
                 bandits: list,
                 seed: Optional[int]=None,
                 epsilon: float=0.1) -> None:
        self.epsilon = epsilon
        super().__init__(bandits, seed)

    def choose(self) -> int:
        """Return the index of the selected bandit."""
        if np.random.random() < self.epsilon:
            return np.random.randint(0, len(self._bandits))
        else:
            return self.best()


class SoftmaxStrategy(Strategy):
    """Pick an bandit according to the Boltzman distribution"""
    def __init__(self,
                 bandits: list,
                 seed: Optional[int]=None,
                 tau: float=0.01) -> None:
        self.tau = tau
        super().__init__(bandits, seed)

    def choose(self) -> int:
        """Return the index of the selected bandit."""

        # try each one at least once, to avoid nans
        if self.scores.trials.min() == 0:
            return self.scores.trials.idxmin()

        probs = np.exp(self.scores.wins / self.scores.trials / self.tau)
        probs /= probs.sum()
        return np.random.choice(range(0, len(self._bandits)), p=probs)


class UCB1Strategy(Strategy):
    """Pick the bandit with the highest Upper Confidence Bound."""
    def _ucb(self) -> pd.Series:
        confidence_bounds = np.sqrt(2 *
                                    np.log(self.scores.trials.sum()) /
                                    self.scores.trials)
        ucb = self.scores.wins / self.scores.trials + confidence_bounds
        return ucb

    def choose(self) -> int:
        """Return the index of the selected bandit."""

        # try each one at least onces, to avoid nans
        if self.scores.trials.min() == 0:
            return self.scores.trials.idxmin()

        return self._ucb().idxmax()


class BayesianStrategy(Strategy):
    """Pick a bandit randomly choosed from the bayesian estimatiion
    of the probabilities."""
    def choose(self) -> int:
        """Return the index of the selected bandit."""
        samples = stats.beta(self.scores.wins + 1,
                           self.scores.trials - self.scores.wins + 1).rvs()

        return np.argmax(samples)
