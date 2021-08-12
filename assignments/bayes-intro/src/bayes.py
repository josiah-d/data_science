import matplotlib.pyplot as plt


class Bayes(object):
    '''
    Args:
        prior (dict): each key is a possible parameter value (e.g. 4-sided
                      die), each value is the associated probability of that
                      parameter value

        likelihood_func (function): takes a new piece of data and a parameter
                                    value, outputs the likelihood of getting
                                    that data given that value of the
                                    parameter
    '''
    def __init__(self, prior, likelihood_func):
        self.prior = prior
        self.likelihood_func = likelihood_func

    def normalize(self):
        '''
        Makes the sum of the probabilities in self.prior equal 1.

        Args: None

        Returns: None

        '''
        pass

    def update(self, data):
        '''
        Conduct a bayesian update. For each possible parameter value
        in self.prior, multiply the prior probability by the likelihood
        of the data and make this the new prior.

        Args:
            data (int): A single observation (data point)

        Returns: None

        '''
        pass

    def print_distribution(self):
        '''
        Print the current posterior probability.
        '''
        pass

    def plot(self, color=None, title=None, label=None):
        '''
        Plot the current prior.
        '''
        pass
