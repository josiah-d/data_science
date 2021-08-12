import numpy as np
from scipy import stats


def make_data(n_features, n_pts, noise=0.0):
    """
    Make fake data for exploring regression. The features (X) are uniformly
    distributed between -1 and 1. The target is a quadratic polynomial of
    all the features with random coefficients, plus normally distributed
    noise (off by default).

    Parameters
    ----------
    n_features: int, number of columns in the output
    n_pts: int, number of rows
    noise: float, normally distributed noise added to y

    Returns
    -------
    (X, y)
    X: numpy array of shape (n_features, n_pts)
    y: numpy array of shape (n_pts)
    """
    X = stats.uniform(-1, 2).rvs((n_pts, n_features))

    # include a feature of 1's, for first-order terms in quadratic
    ones = np.ones((n_pts, 1))
    X_plus_ones = np.concatenate([ones, X], axis=1)

    # random coefficient matrix
    coeffs = stats.uniform(-1, 2).rvs((n_features+1, n_features+1))

    y = (X_plus_ones.reshape(n_pts, n_features+1, 1) *
         coeffs *
         X_plus_ones.reshape(n_pts, 1, n_features+1)).sum(axis=(1, 2))
    y += stats.norm(0, noise).rvs(n_pts)
    return X, y
