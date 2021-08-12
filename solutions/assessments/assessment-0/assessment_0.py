'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-0)
  Then run the tests with this command: "make test"
'''


def fizz_buzz():
    '''
    INPUT: None 
    OUTPUT: LIST

    Write a program that appends the numbers from 1 to 100 into list. 
    But for multiples of three append “Fizz” instead of the number and 
    for the multiples of five append “Buzz”. For numbers which are 
    multiples of both three and five append “FizzBuzz”.

    The first five elements of your list should be:
    lst = [1, 2, "Fizz", 4, "Buzz", ....]
    '''
    lst = [] 
    for i in range(1, 101):
        div3 = i % 3 == 0
        div5 = i % 5 == 0
        div3and5 = div3 and div5
        if div3and5:
            lst.append("FizzBuzz")
        elif div3:
            lst.append("Fizz")
        elif div5:
            lst.append("Buzz")
        else:
            lst.append(i)
    return lst


def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary which contains a count of the number of times 
    each character appears in the string. Characters which with a count 
    of 0 should not be included in the output dictionary.
    '''
    d = {}
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


def merge_dictionaries(d1, d2):
    '''
    INPUT: dictionary, dictionary
    OUTPUT: dictionary

    Return a new dictionary which contains all the keys from d1 and d2 
    with their associated values. If a key is in both dictionaries, the 
    value should be the sum of the two values.
    '''
    d = d1.copy()
    for key, value in d2.items():
        d[key] = d.get(key, 0) + value
    return d
    # Another solution:
    # return {k: d1.get(k, 0) + d2.get(k, 0) for k in (set(d1) | set(d2))}


def cookie_jar(a, b):
    '''
    INPUT: FLOAT (probability of drawing a chocolate cooking from Jar 
                  A),
           FLOAT (probability of drawing a chocolate cooking from Jar 
                  B)
    OUTPUT: FLOAT (conditional probability that cookie was drawn from 
                   Jar A given that a chocolate cookie was drawn)

    There are two jars of cookies.
    Each has chocolate and peanut butter cookies.
    INPUT 'a' is the fraction of cookies in Jar A which are chocolate
    INPUT 'b' is the fraction of cookies in Jar B which are chocolate
    A jar is chosen at random and a cookie is drawn.
    The cookie is chocolate.
    Return the probability that the cookie came from Jar A.
    '''

    return a / (a + b)


def boolean_indexing(arr, minimum):
    '''
    INPUT: NUMPY ARRAY, INT
    OUTPUT: NUMPY ARRAY
    (of just elements in "arr" greater or equal to "minimum")

    Return an array of only the elements of "arr" that are greater than 
    or equal to "minimum"

    Ex:
    In [1]: boolean_indexing(np.array([[3, 4, 5], [6, 7, 8]]), 7)
    Out[1]: array([7, 8])
    '''
    return arr[arr >= minimum]


def size_of_multiply(a, b):
    '''
    input: 2 dimensional numpy array, 2 dimensional numpy array
    output: tuple

    if matrices a (dimensions m x n) and b (dimensions p x q) can be 
    multiplied (ab), return the shape of the result of multiplying 
    them. use the shape function. do not actually multiply the 
    matrices, just return the shape.

    if a and b cannot be multiplied, return none.
    '''
    if a.shape[1] == b.shape[0]:
        return a.shape[0], b.shape[1]
    return None


def data_frame_work(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA 
    and colB.
    Assume that df contains columns colA and colB and that these are 
    numeric.
    '''
    df[colC] = df[colA] + df[colB]
