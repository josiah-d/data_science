from bayes import Bayes


def die_likelihood(roll, die):
    """
    Args:
        roll (int): result of a single die roll
        die  (int): number of sides of the die that produced the roll

    Returns:
        likelihood (float): the probability of the roll given the die.
    """
    pass  # fill in here


if __name__ == '__main__':
    prior_1 = {}  # fill in here
    prior_2 = {}  # fill in here
    die_bayes_1 = Bayes(prior_1, die_likelihood)
    # ... you take it from here ...
