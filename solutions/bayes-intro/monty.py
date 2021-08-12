import random


class Monty(object):
    def __init__(self):
        '''
        Initialize instance variables:
        doors: list of strings
        wins: integer
        total: integer
        '''
        self.doors = ['a', 'b', 'c']
        self.wins = 0
        self.total = 0

    def play(self, strategy, chosen='a'):
        '''
        INPUT: function, string
        OUTPUT: Boolean

        Play the Monty Hall game once. The first choice is given by the
        argument chosen. Randomly choose a prize door and an empty door to
        reveal. The users strategy is given by the function strategy which
        takes a list of the door names, the prize door, and the door that was
        shown to be empty.

        Update the counters according to the results of the game and return
        True if the player wins, False otherwise.
        '''
        prize = random.choice(self.doors)
        empty = (set(self.doors) - {prize, chosen}).pop()
        self.total += 1
        if strategy(self.doors, chosen, empty) == prize:
            self.wins += 1
            return True
        return False

    def play_n_times(self, n, strategy):
        '''
        INPUT: integer, function
        OUTPUT: None

        Play the Monty Hall game n times.
        '''
        for i in range(n):
            self.play(strategy)
        output = "Total wins: {}, Total trials: {}, Percent wins: {}"
        return output.format(self.wins,
                             self.total,
                             float(self.wins) / self.total)
