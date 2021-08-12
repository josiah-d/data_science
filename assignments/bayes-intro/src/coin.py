import random


class Coin(object):

    # secret probability
    prob = 0b111000 / 0b1100100

    def flip(self):
        if random.random() < self.prob:
            return 'H'
        else:
            return 'T'
