import pytest
import numpy as np
from src.bandit import Bandit

def test_bandit_pull(p=.5, n_pulls=1000):
    """Bandit returns either True or False on each pull."""
    bandit = Bandit(p=p)
    assert all(bandit.pull() in (True, False) for _ in range(n_pulls))

def test_bandit_expected_value(p=.5, n_pulls=1000):
    """Observed probability of success is similar to expected probability of success."""
    bandit = Bandit(p=p)
    observed = sum(bandit.pull() for _ in range(n_pulls))
    std = np.sqrt(n_pulls * p * (1-p))
    expected = pytest.approx(n_pulls*p, 3*std)
    assert observed == expected

def test_bandit_probability_zero(n_pulls=1000):
    """Bandit with probability zero always returns False."""
    bandit = Bandit(p=0)
    assert all(bandit.pull() is False for _ in range(n_pulls))

def test_bandit_probability_one(n_pulls=1000):
    """Bandit with probability one always returns True."""
    bandit = Bandit(p=1)
    assert all(bandit.pull() is True for _ in range(n_pulls))

