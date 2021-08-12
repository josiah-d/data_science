import matplotlib.pyplot as plt
import random

class Bayes(object):
    '''
    INPUT:
        prior (dict): key is the value (e.g. 4-sided die),
                      value is the probability
    '''
    def __init__(self, prior):
        self.prior = prior
        

    def likelihood_func(self, single_data_point, parameter_value):
        """
        INPUT:
            single_data_point (int): One roll to determing the likelihood of

            parameter_value (int): Key in the prior dict of a die to check the roll on

        OUTPUT:
            (int, float): Likelihood of getting the data point given a certain die
        """
        if single_data_point > parameter_value: # Roll is outside the scope of the die, so P(Roll | Die) = 0
            return 0
        return 1/parameter_value

    def normalize(self):
        '''
        INPUT: None
        OUTPUT: None

        Makes the sum of the probabilities equal 1.
        '''
        total = float(sum(self.prior.values()))
        for key in self.prior:
            self.prior[key] /= total

    def update(self, data):
        '''
        INPUT:
            data (int or str): A single observation (data point)

        OUTPUT: None
        
        Conduct a bayesian update. Multiply the prior by the likelihood and
        make this the new prior.
        '''
        for key in self.prior:
            self.prior[key] *= self.likelihood_func(data, key)
        self.normalize()

    def print_distribution(self):
        '''
        Print the current posterior probability.
        '''
        sorted_keys = sorted(self.prior.keys())
        for key in sorted_keys:
            print('{0}: {1:0.2f}'.format(key, self.prior[key]))

    def plot(self, color=None, title=None, label=None):
        '''
        Plot the current prior.
        '''
        sorted_keys = sorted(self.prior.keys())
        sorted_probs = [self.prior[key] for key in sorted_keys]
        plt.plot(sorted_keys, sorted_probs, color=color, label=label)
        plt.title(title)

def roll_die(sides):
    num = random.randint(1,sides)
    print(f"\nRolled a {num}.")
    return num

def find_max_prior(prior):
    max_prior = 0
    for k,v in prior.items():
        if v > max_prior:
            max_prior = v
            max_key = k
    return max_key

if __name__ == '__main__':
    prior = {4: 0.2, 6: 0.2, 8: 0.2, 12: 0.2, 20: 0.2}
    bayes_updater = Bayes(prior)
    print("Here's the prior:") 
    bayes_updater.print_distribution()
    die = random.choice(list(prior.keys()))
    print(f"Picked the {die}-sided die.")
    threshold = 0.9 # probability threshold for picking a die 

    max_prior = max(prior.values())
    while max_prior < threshold:
        roll = roll_die(die)
        bayes_updater.update(roll)
        bayes_updater.print_distribution()
        max_prior = max(prior.values())
    die_believed = find_max_prior(prior)
    print(f"\nFrom the rolls, I believe it's a {die_believed}-sided die.")
    print(f"It's actually a {die}-sided die.")

        
