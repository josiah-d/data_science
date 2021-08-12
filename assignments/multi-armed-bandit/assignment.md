# Multi-Armed Bandit

- [Multi-Armed Bandit](#multi-armed-bandit)
  - [Introduction](#introduction)
  - [Basic](#basic)
    - [Part 1: Implement each strategy](#part-1-implement-each-strategy)
    - [Part 2: Count wins](#part-2-count-wins)
  - [Advanced](#advanced)
    - [Part 3: Measure regret](#part-3-measure-regret)
    - [Part 4: Plot win ratio](#part-4-plot-win-ratio)
  - [Extra Credit](#extra-credit)
    - [Part 5: Evaluate success](#part-5-evaluate-success)

## Introduction

In this assignment you'll implement various strategies for addressing the multi-armed bandit problem, specifically working with "binary bandits" where there is a single winner.

There are a couple notes about the code in this assignment. First, it makes use of inheritance. Although inheritance is critical in many object-oriented languages, python's use of duck typing makes it largely irrelevant. In this case, however, strategies will inherit methods from base classes, so the use of inheritance will simplify the implementation.

Second, the existing code makes heavy use of type hints. Although you can ignore these, following the convention will give you practice in using them in the future. You can verify type hints with `mypy`.

## Basic

### Part 1: Implement each strategy

Fill in the code stubs in `banditstrategy.py`. This already includes a completed base Strategy class as well as two trivial strategies that inherit from it: RandomStategy and GreedyStrategy. The `Bandit` class (completed) is in `bandit.py`. You can simulate running the multi-arm bandit with the following code. We are creating three versions of the site with conversion rates of 5%, 3% and 6%. Hopefully one of the other strategies will learn that the last one is the best.

For each class, you'll need to redefine the `choose` method, and maybe the `__init__` method as well if the strategy requires parameters. Note that the stub files include optional type hints; you can include them or not. If you use them, run the `mypy` program to verify they work (you can ignore errors about library stub files).

```python
from bandit import Bandit
import banditstrategy

bandits = [Bandit(p) for p in [0.05, 0.03, 0.06]]
strat = banditstrategy.RandomStrategy(bandits)
strat.sample(1000)
scores = strat.scores
print(scores)
```

Fill in the code stubs to implement the four strategies: epsilon-greedy, softmax, ucb1 and bayesian bandits. If you need a reminder of how any of the algorithms work, take a look at the lecture notes.

### Part 2: Count wins

See how many wins you have of the 1000 trials using each of the six strategies (two already implemented) with the starting bandits given above.

> Try running it again with all of these values below as `probabilities` and see how different each algorithm does with respect to total number of wins in 1000 rounds.

```csv
[0.1, 0.1, 0.1, 0.1, 0.9]
[0.1, 0.1, 0.1, 0.1, 0.12]
[0.1, 0.2, 0.3, 0.4, 0.5]
```

## Advanced

### Part 3: Measure regret

Here is a method to calculate the **regret** after each iteration.
Add this to the base `Strategy` class. For more information about the `cumsum()` method, check the official [doc](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html).

```python
import numpy as np

def regret(self):
    """Return the regrets over time as a numpy array, defined as the difference of
    the optimal expected value (if the best bandit were chosen)
    and the expected value given the choices made."""
    probabilities = np.array([bandit.p for bandit in self._bandits])
    p_opt = probabilities.max()
    return np.cumsum(p_opt -
                     probabilities[self._choices])
```

- Do you need to change the other classes implementing the various strategies to use this?

- Use matplotlib to plot the total regret over time of each algorithm. Use the Bandits with these hidden probabilities: `[0.05, 0.03, 0.06]`

### Part 4: Plot win ratio

Plot the percentage of times the optimal bandit was chosen over time. For example, after 100 trials, what is the percentage that the optimal bandit is picked for a specific strategy?

## Extra Credit

### Part 5: Evaluate success

Experiment with the number of trials and hidden probabilities to compare the four strategies you implemented:

- epsilon-greedy
- softmax
- ucb1
- bayesian bandits

Given a variety of situations (number of trials, difference in conversion rate) which one performs better? Why?
