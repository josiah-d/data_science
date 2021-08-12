import random

class Coin(object):
    def flip(self):
        if random.random() < 0.56:
            return 'H'
        else:
            return 'T'
