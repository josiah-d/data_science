'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-6)
  Then run the tests with this command: "make test"
'''


def get_diagonal(mat):
    '''
    INPUT: 2 dimensional list
    OUTPUT: list

    Given a matrix encoded as a 2 dimensional python list, return a list
    containing all the values in the diagonal starting at the index 0, 0.

    E.g.
    mat = [[1, 2], [3, 4], [5, 6]]
    | 1  2 |
    | 3  4 |
    | 5  6 |
    get_diagonal(mat) => [1, 4]

    You may assume that the matrix is nonempty.
    '''
    return [mat[i][i] for i in range(min(len(mat), len(mat[0])))]


from sklearn.model_selection import train_test_split
def same_proportion_minority_class(X, y, test_size=0.2):
    '''Performs a train-test split on the X and y data, returning:
    X_train, X_test, y_train, y_test in that order.
    default split should be 80%-20%

    However, the target y is categorical (0 and 1) and there is a large
    class imbalance.  So train-test split is specified such that the
    proportion of the minority class is preserved between the train and
    test sets.

    You may use imports for this question.

    Parameters
    ----------
    X, y: NumPy Array, NumPy Array

    Returns
    -------
    X_train, X_test, y_train, y_test:
        NumPy Array, NumPy Array, NumPy Array, NumPy Array
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        stratify=y)
    return X_train, X_test, y_train, y_test


def filtered_market_count():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives the number of markets that do not have 
    'Farmers Market' in its name. Please only include markets in states with a 
    large population in 2010 (greater than 20,000,000).
    '''

    return '''SELECT COUNT(*)
                FROM farmersmarkets AS fm
                JOIN statepopulations AS sp
                ON sp.state = fm.State
                WHERE sp.pop2010 > 20000000 AND
                      fm.MarketName NOT LIKE '%Farmers Market%';
           '''


def market_density_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives a table containing each state, number
    of people per farmers market (using the population number from 2010).
    If a state does not appear in the farmersmarket table, it should still
    appear in your result with a count of 0.
    '''

    return '''
             SELECT p.state, COALESCE(p.pop2010 / m.cnt, 0)
               FROM statepopulations p
               LEFT OUTER JOIN (
                 SELECT state, COUNT(1) AS cnt
                   FROM farmersmarkets 
                   GROUP BY state) m 
                 ON p.state=m.state
            ;
           '''

# Alternate queries for edification
#     return '''
#            -- Replace COALESCE from previous example with CASE WHEN
#            SELECT p.State, 
#                 CASE 
#                   WHEN m.cnt IS NULL THEN 0
#                   ELSE pop2010 / m.cnt 
#                 END
#               FROM statepopulations p
#                 LEFT OUTER JOIN (
#                   SELECT state, COUNT(1) AS cnt
#                     FROM farmersmarkets
#                     GROUP BY state) m 
#                   ON p.State = m.state
#             ;
#            '''
# 
#     return '''
#            -- Remove subquery from previous example
#            -- Flip join order
#            SELECT p.State, 
#                CASE 
#                  WHEN COUNT(FMID) = 0 THEN 0 
#                  ELSE pop2010 / COUNT(FMID) 
#                END
#              FROM farmersmarkets m
#                RIGHT OUTER JOIN statepopulations p 
#                  ON p.State = m.state
#              GROUP BY p.State, pop2010
#            ;
#            '''
# 
#     return '''
#            -- Replace CASE WHEN from previous example with COALESCE
#            -- Use FULL JOIN instead of LEFT JOIN or RIGHT JOIN
#            SELECT p.State, COALESCE(pop2010 / NULLIF(COUNT(FMID), 0), 0) 
#              FROM farmersmarkets m
#                FULL JOIN statepopulations p 
#                  ON p.State = m.state
#              GROUP BY p.State, pop2010
#            ;
#            '''