'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-4)
  Then run the tests with this command: "make test"
'''


from sklearn.linear_model import LinearRegression
def linear_regression(X_train, y_train, X_test, y_test):
    '''
    Fit a linear regression model with X_train and y_train using
    scikit-learn, and return the beta coefficients. Then calculate and
    return the R^2 value using X_test and y_test.

    Parameters
    ----------
    X_train: NumPy Array (size: N x P)
    y_train: NumPy Array (size: N x 1)
    X_test: NumPy Array (size: M x P)
    y_test: NumPy Array (size: M x 1)
   
    Returns
    -------
    tuple of floats, float
    The tuple contains the beta coefficients of the fit model, and the
    remaining float is the R^2 value of the test data using that model.
    
    Note
    ----
    The R^2 statistic, also known as the coefficient of determination, is a
    popular measure of fit for a linear regression model.  If you need a
    refresher, this wikipedia page should help:
    https://en.wikipedia.org/wiki/Coefficient_of_determination
    '''
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    return regr.coef_, regr.score(X_test, y_test)


def sql_count_neighborhoods():
    '''
    INPUT: None
    OUTPUT: string

    Return a SQL query that gives the number of neighborhoods in each city
    according to the rent table. Keep in mind that city names are not always
    unique unless you include the state as well, so your result should have
    these columns: city, state, cnt
    '''
    return '''SELECT city, state, COUNT(1) AS cnt
              FROM rent
              GROUP BY city, state;'''