import scipy.stats as scs
import numpy as np
import pandas as pd
import random
from typing import List, Optional


class Strategy(object):
    """Strategy for solving the Multi-Armed Bandit Problem."""

    def __init__(self, bandits: list, seed: Optional[int] = None) -> None:
        """
        Parameters
        ----------
        bandits: list of Bandit objects,
                  each with a pull method that returns a bool.
        seed:     int to initialize random number generator."""
        self._bandits = bandits
        self.seed = seed
        self._choices = []  # type: List[int]
        self._results = []  # type: List[bool]
        self.scores = pd.DataFrame(np.zeros((len(self._bandits), 2)),
                                   columns=['trials', 'wins'])
        # seed the random number generators so you get the same results every
        # time.
        if seed:
            np.random.seed(self.seed)
            random.seed(self.seed)

    def sample(self, n: int = 1) -> None:
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
    Pick a bandit randomly with equal probability with probability epsilon.
    Otherwise pick the bandit with the best observed proportion of winning.
    """
    def __init__(self,
                 bandits: list,
                 seed: Optional[int] = None,
                 epsilon: float = 0.1) -> None:
        self.epsilon = epsilon
        super().__init__(bandits, seed)

    def choose(self) -> int:
        """Return the index of the selected bandit."""
        pass


class SoftmaxStrategy(Strategy):
    """Pick a bandit according to the Boltzman distribution"""
    def __init__(self,
                 bandits: list,
                 seed: Optional[int] = None,
                 tau: float = 0.01) -> None:
        # code is needed here
        pass

    def choose(self) -> int:
        """Return the index of the selected bandit."""
        pass


class UCB1Strategy(Strategy):
    """Pick the bandit with the highest Upper Confidence Bound."""
    def choose(self) -> int:
        """Return the index of the selected bandit."""
        pass


class BayesianStrategy(Strategy):
    """Pick a bandit randomly choosed from the bayesian estimatiion
    of the probabilities."""
    def choose(self) -> int:
        """Return the index of the selected bandit."""
        pass
