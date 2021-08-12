'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-5)
  Then run the tests with this command: "make test"
'''


def sum_to_target(nums, target):
    '''
    Given an array of integers and a target integer, return 
    indices of the two numbers in the array that sum to equal 
    the target.

    You may assume that each input would have exactly one solution,  
    and you may not use an element at the same index more than once.
    
    Return the indices in ascending order.   
    For full points your solution should have a runtime of O(N). 

    Parameters
    ----------
    nums: list
    target: int

    Returns
    -------
    list
    
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    '''
    # Need to keep track of the index of numbers we've seen. 
    index = {}
    for i,  num in enumerate(nums):
        looking_for = target - num
        if looking_for in index:
            return [index[looking_for], i]
        else:
            index[num] = i
            

def split_node(X, y, col, split_val):
    '''
    INPUT: NUMPY ARRAY, NUMPY ARRAY, INT, FLOAT
    OUTPUT: NUMPY ARRAY, NUMPY ARRAY, NUMPY ARRAY, NUMPY ARRAY

    Split a feature matrix X and the target array y into "left" and "right"
    arrays determined by splitting on "split_val" in col of the X matrix.
    The "left" matrices of X and y contain the rows corresponding to values in 
    col <= split value, while the "right" matrices contain the rows where
    col > split value.  Return the four arrays separately (see example
    below).

    You can assume that all columns in X are continuous values.  col is
    an integer (0 indexed) that indicates which column of X to use to split
    the X and y arrays.

    Return empty arrays for the left or right arrays if no values are returned.
    
    Ex:
    In [1]: X = np.array([[ 5.5,  2.4,  3.7],
                          [ 5.5,  2.3,  3.8],
                          [ 6.1,  3.0,  4.9],
                          [ 5.2,  3.5,  1.5],
                          [ 5.7,  2.6,  3.5]])
    
    In [2]: y = np.array([1, 1, 2, 0, 1])
    
    In [3]: X_left, y_left, X_right, y_right = split_node(X, y, 1, 2.6)

    In [4]: X_left
    Out[4]:
    array([[5.5, 2.4, 3.7],
           [5.5, 2.3, 3.8],
           [5.7, 2.6, 3.5]])
    
    In [5]: y_left
    Out[5]: array([1, 1, 1])

    '''
    left = X[:, col] <= split_val
    right = ~left
    return X[left], y[left], X[right], y[right]


import numpy as np
def calculate_entropy(arr):
    '''
    INPUT: NUMPY ARRAY of binary values (0 and 1)
    OUTPUT: FLOAT

    Return the Shannon entropy of a numpy array containing only two classes
    (integers 0 and 1).

    You can assume that the array will always contain one or more values.
    '''
    # solution is for an arbitrary number of classes 
    num_val = len(arr) 
    classes = np.unique(arr)
    probs = [len(arr[arr==cls])/num_val for cls in classes]
    return -1*sum([p*np.log2(p) for p in probs])
    

import numpy as np    
import pandas as pd
def make_series(start, length, index):
    '''
    INPUTS: INT, INT, LIST (of length "length")
    OUTPUT: PANDAS SERIES (of "length" sequential integers
             beginning with "start" and with index "index")

    Create a pandas Series of length "length" with index "index"
    and with elements that are sequential integers starting from "start".
    You may assume the length of index will be "length".

    E.g.,
    In [1]: make_series(5, 3, ['a', 'b', 'c'])
    Out[1]:
    a    5
    b    6
    c    7
    dtype: int64
    '''
    return pd.Series(np.arange(length) + start, index=index)
    
    
def sql_highest_rent_increase():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the 5 San Francisco neighborhoods with the
    highest rent increase.
    '''
    return '''SELECT neighborhood
              FROM rent
              WHERE city='San Francisco'
              AND rent.med_2014 - rent.med_2011 IS NOT NULL
              ORDER BY med_2014-med_2011 DESC LIMIT 5;'''


def sql_rent_and_buy():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the rent price and buying price for 2014 for
    all the neighborhoods in San Francisco.
    Your result should have these columns:
        neighborhood, rent, buy
    '''
    return '''SELECT a.neighborhood, a.med_2014 AS rent, b.med_2014 AS buy
              FROM rent a
              JOIN buy b
              ON a.neighborhood=b.neighborhood AND a.city=b.city AND a.state=b.state
              WHERE a.city='San Francisco';'''
