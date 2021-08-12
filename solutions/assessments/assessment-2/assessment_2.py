'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-2)
  Then run the tests with this command: "make test"
'''


from numpy import random
import numpy as np
def roll_the_dice(n_simulations = 1000):
    '''
    input: int
    output: float

    two unbiased, six sided, dice are thrown once and the sum of the 
    showing faces is observed (so if you rolled a 3 and a 1, you would 
    observe the sum, 4). use a simulation to find the estimated 
    probability that the total score is an even number or a number 
    greater than 7.  your function should return an estimated 
    probability, based on rolling the two dice n_simulations times.
    '''
    total = 0
    num_repeats = 10000
    for i in range(num_repeats):
        die1 = random.randint(1, 6+1)
        die2 = random.randint(1, 6+1)
        score = die1 + die2
        if score % 2 == 0 or score > 7:
            total += 1
    return float(total) / num_repeats
    # with numpy operations
    # two_dice_sum = np.random.randint(1, 7, (2, 10000)).sum(axis=0)
    # return np.logical_or(two_dice_sum > 7, np.logical_not(two_dice_sum % 2)).mean()


import numpy as np
def return_percentage_greater_than_80(arr):
  '''
  Return the percentage of the rows in arr where the sum of the two values is greater than 80. 
  *You should use numpy to do this.* 

  Parameters
  ==========
  arr: 2 dimensional numpy array

  Returns
  ======
  percentage: float
  '''
  return sum(np.sum(arr, axis = 1) > 80)/len(arr)*100



import numpy as np
def only_positive(arr):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing only the rows from arr where all 
    the values in that row are positive.

    E.g.  np.array([[1, -1, 2], 
                    [3, 4, 2], 
                    [-8, 4, -4]])
              ->  np.array([[3, 4, 2]])

    Use numpy methods to do this, full credit will not be awarded for a 
    python for loop.
    '''
    return arr[np.min(arr, 1) > 0]

import pandas as pd
def pandas_query(df):
    '''
    input: dataframe
    output: dataframe

    given a dataframe containing university data with these columns:
        name, address, website, type, size

    return the dataframe containing the average size for each 
    university type ordered by average size in ascending order.
    '''
    return df.groupby('Type').mean().sort_values(by='Size')
    # alternative:
    # return df.groupby("Type")["Size"].mean().sort_values()

import pandas as pd
def return_loans_by_id(df):
    '''
    Takes a df and returns a df for loans with the IDs '7484', '4423', and '9910'.
    The dataframe’s index has been set to be the loan IDs (a string). 
    Parameters
    ==========
    df: Pandas DataFrame

    Returns
    =======
    Pandas DataFrame
    '''
    return df.loc[['7484', '4423', '9910']]


import pandas as pd
def return_loans(df):
    '''
    Takes a df and returns data at the 0th, 1st, and 4th indices.

    Parameters
    ==========
    df: Pandas DataFrame

    Returns
    =======
    Pandas DataFrame
    '''
    return df.iloc[[0, 1, 4]]

