'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-3)
  Then run the tests with this command: "make test"
'''


def divisible_by(arr, int1, int2):
    '''
    INPUT: NUMPY ARRAY, INT, INT
    OUTPUT: NUMPY ARRAY
    
    arr in a numpy array of integers.  int1 and int2 are integers. 
    Return an array of the integers in arr that are divisible without 
    remainder by both int1 and int2. 

    For example:
    In [1] arr_out = divisible_by(np.array([0, 24, 3, 12, 18, 17]), 3, 4)
    In [2] arr_out
    Out[2] np.array([0, 24, 12])
    '''
    return arr[(arr%int1==0) & (arr%int2==0)]

###### not used in Feb 20201 cohort ############

def bubble_sort(arr):
    '''
    INPUT: LIST
    OUTPUT: LIST OF LISTS

    Implement the bubble sort algorithm to sort arr.  However, upon on 
    each swap, append the new list as the next row in a list 
    containing all the swaps. The original list should be the first row 
    in the list detailing the swaps.

    For example:
    In [1] arr = [7, 4, 2, 5]
    In [2] bs = bubble_sort(arr)
    In [3] bs
    Out[3]
    [[7, 4, 2, 5],
     [4, 7, 2, 5],
     [4, 2, 7, 5],
     [4, 2, 5, 7],
     [2, 4, 5, 7]]

    ''' 
    arr_lst = []
    arr_lst.append(arr.copy())
    for i in range(len(arr), 0, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
                arr_lst.append(arr.copy())
    return(arr_lst)

#############################################

def sql_query():
    '''
    input: none
    output: string

    given a table named universities which contains university data 
    with these columns:

        name, address, website, type, size

    return a sql query that gives the average size of each university 
    type in ascending order.
    '''
    # your code should look like this:
    # return '''select * from universities;'''
    return '''select 
                type, 
                avg(size) as avg_size 
              from universities 
              group by type 
              order by avg_size;
           '''


def markets_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING (of SQL statement)

    Return a SQL statement which gives the states and the number of 
    markets for each state which take WIC or WICcash.
    '''

    return '''SELECT State, COUNT(1)
              FROM farmersmarkets
              WHERE WIC='Y' OR WICcash='Y'
              GROUP BY State;'''

### moved from assessment 2 to assessment 3 in Feb 2020 cohort ####

import scipy.stats as stats
def calculate_t_test(sample1, sample2, type_i_error_rate):
    '''
    input: numpy array, numpy array
    output: float, boolean
    you are asked to evaluate whether the two samples come from a 
    population with the same population mean.  return a tuple 
    containing the p-value for the pair of samples and true or false 
    depending if the p-value is considered significant at the provided 
    type i error rate (i.e. false positive rate, i.e. alpha).
    '''
    _, pvalue = stats.ttest_ind(sample1, sample2)
    return pvalue, pvalue < type_i_error_rate