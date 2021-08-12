'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-1)
  Then run the tests with this command: "make test"
'''


def max_lists(list1, list2):
    '''
    INPUT: list, list
    OUTPUT: list

    list1 and list2 have the same length. Return a list which contains 
    the maximum element of each list for every index.
    '''
    return [max(i1, i2) for i1, i2 in zip(list1, list2)]


def invert_dictionary(d):
    '''
    INPUT: DICT
    OUTPUT: DICT (of sets of input keys indexing the same input values
                  indexed by the input values)

    Given a dictionary d, return a new dictionary with d's values as 
    keys and the value for a given key being the set of d's keys which 
    shared the same value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    result = {}
    for key, value in d.items():
        if value not in result:
            # We use a set since original keys had no duplicates
            result[value] = set()
        # We can now safely call the .add method
        result[value].add(key)
    return result


def matrix_multiplication(A, B):
    '''
    INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS,
            LIST (of length n) OF LIST (of length n) OF INTEGERS
    OUTPUT: LIST OF LIST OF INTEGERS
            (storing the product of a matrix multiplication operation)

    Return the matrix which is the product of matrix A and matrix B 
    where A and B will be (a) integer valued (b) square matrices (c) of 
    size n-by-n (d) encoded as lists of lists,  e.g.
    A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix
    | 2  3  4 |
    | 6  4  2 |
    |-1  2  0 |
    
    YOU MAY NOT USE NUMPY. Write your solution in straight python.
    '''

    n = len(A)
    result = []
    # iterate over the rows of A
    for i in range(n):
        row = []
        # iterate over the columns of B
        for j in range(n):
            total = 0
            # iterate ith row of A with jth column of B dot product
            for k in range(n):
                # k implements [ith row][jth column] element-wise dot product
                total += A[i][k] * B[k][j]
            # column j of row i
            row.append(total)
        # all columns j of row i completed
        result.append(row)
    # all rows done
    return result


def reverse_index(arr, finRow, finCol):
    '''
    INPUT: NUMPY ARRAY, INT, INT
    OUTPUT: NUMPY ARRAY (of an upside down subset of "arr")

    Reverse the row order of "arr" (i.e. so the top row is on the 
    bottom) and return the sub-matrix from coordinate [0, 0] up to 
    (but not including) [finRow, finCol].

    Ex:
    In [1]: arr = np.array([[ -4,  -3,  11],
                            [ 14,   2, -11],
                            [-17,  10,   3]])
    In [2]: reverse_index(arr, 2, 2)
    Out[2]:
    array([[-17, 10],
           [ 14,  2]])

    Hint: this can be using two steps of slicing that can be combined 
    into a one-liner.
    '''
    return arr[::-1][:finRow, :finCol]


import numpy as np
def array_work(rows, cols, scalar, matrixA):
    '''
    INPUT: INT, INT, INT, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY
    (of matrix product of r-by-c matrix of "scalar"'s time matrixA)

    Create matrix of size (rows, cols) with elements initialized to the 
    scalar value. Right multiply that matrix with the passed matrixA 
    (i.e. AB, not BA).  Return the result of the multiplication. You 
    needn't check for matrix compatibililty, but you accomplish this in 
    a single line.


    E.g., array_work(2, 3, 5, np.array([[3, 4], [5, 6], [7, 8]]))
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
    '''
    return matrixA.dot(np.ones((rows, cols)) * scalar)


def pandas_add_increase_column(df):
    '''
    INPUT: DataFrame
    OUTPUT: None

    Add a column to the DataFrame called 'Increase' which contains the 
    amount that the median rent increased by from 2011 to 2014.
    '''
    df['Increase'] = df['med_2014'] - df['med_2011']
    # Another solution:
    # df.eval('Increase = med_2014 - med_2011', inplace=True)


def pandas_max_rent(df):
    '''
    INPUT: DataFrame
    OUTPUT: DataFrame

    Return a new pandas DataFrame which contains every city and the 
    highest median rent from that city for 2011 and 2014.
    Your DataFrame should contain these columns:
        City, State, med_2011, med_2014

    '''
    return df[['City', 'State', 'med_2011', 'med_2014']].groupby(['City', 'State']).max()

    # Another solution:
    # return df.groupby(['City', 'State']).max().reset_index()[['City', 'State', 'med_2011', 'med_2014']]
