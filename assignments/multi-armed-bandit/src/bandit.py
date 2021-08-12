"""A single One-Armed Bandit."""
import random


class Bandit(object):
    """A binary random variable that returns True with probability p."""

    def __init__(self, p: float) -> None:
        """Create a new Bandit with probability p."""
        self.p = p

    def __repr__(self) -> str:
        return f'Bandit(p={self.p})'

    def pull(self) -> bool:
        """Return True or False with probabilities (p, 1-p)."""
        return random.random() < self.p
