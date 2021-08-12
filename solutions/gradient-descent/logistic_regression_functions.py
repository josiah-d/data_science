import numpy as np


def predict_proba(X, coeffs):
    """Calculate the predicted conditional probabilities (floats between 0 and
    1) for the given data with the given coefficients.

    Parameters
    ----------
    X: ndarray, shape (n_samples, n_features)
        The data (independent variables) to use for prediction.
    coeffs: ndarry, shape (n_features, )
        The hypothesised coefficients.

    Returns
    -------
    predicted_probabilities: (n_samples, )
       The conditional probabilities from the logistic hypothosis function
       given the data and coefficients.
    """
    linear_predictor = np.dot(X, coeffs)
    denom = 1 + np.exp(-linear_predictor)
    return 1 / denom


def predict(X, coeffs, threas=0.5):
    """
    Calculate the predicted class values (0 or 1) for the given data with the
    given coefficients by comparing the predicted probabilities to a given
    threashold.

    Parameters
    ----------
    X: ndarray, shape (n_samples, n_features)
        The data (independent variables) to use for prediction.
    coeffs: ndarry, shape (n_features, )
        The hypothesised coefficients.
    threas: float
        Threashold for comparison of probabilities.

    Returns
    -------
    predicted_class: int.  Zero or one.
        The predicted class.
    """
    probs = predict_proba(X, coeffs)
    return probs >= threas


def cost(X, y, coeffs, lam=0.0, has_intercept=True):
    """
    Calculate the total logistic cost function of the data with the given
    coefficients.

    Parameters
    ----------
    X: ndarray, shape (n_samples, n_features)
        The data (independent variables) to use for prediction.
    y: ndarray, shape (n_samples, )
        The actual class values of the response.  Must be encoded as 0's and
        1's.
    coeffs: ndarray, shape (n_features)
        The hypothosized coefficients of the logistic regression.
    lam: float 
        Strength of regularization parameter for the ridge penalty.
    has_intercept: boolean 
        Is the first entry of coeffs an intercept parameter?

    Returns
    -------
    logistic_cost: flaot
        The computed logistic cost.
    """
    p = predict_proba(X, coeffs)
    cost_per_observation = y * np.log(p) + (1 - y) * np.log(1 - p)
    ridge_penalty = np.sum(coeffs*coeffs)
    if has_intercept:
        ridge_penalty -= coeffs[0]*coeffs[0]
    return -np.sum(cost_per_observation) + lam * ridge_penalty


def cost_one_datapoint(x, y, coeffs):
    """
    Calculate the logistic cost function of a single data point using the given
    coefficients.

    Parameters
    ----------
    x: ndarray, shape (n_features, )
        The data (independent variables) to use for prediction.
    y: Integer, 0 or 1 
        The actual class values of the response.
    coeffs: ndarray, shape (n_features)
        The hypothosized coefficients of the logistic regression.

    Returns
    -------
    logistic_cost: float
        The computed logistic cost.
    """
    linear_pred = np.sum(x * coeffs)
    p = 1 / (1 + np.exp(-linear_pred))
    return (- y * np.log(p) - (1 - y) * np.log(1 - p))


def gradient(X, y, coeffs, lam=0.0, has_intercept=True):
    """
    Calculate the gradient of the logistic cost function at the given value for
    the coeffs.

    Parameters
    ----------
    X: ndarray, shape (n_samples, n_features)
        The data (independent variables) to use for prediction.
    y: ndarray, shape (n_samples, )
        The actual class values of the response.  Must be encoded as 0's and
        1's.
    coeffs: ndarray, shape (n_features)
        The hypothosized coefficients of the logistic regression.
    lam: float 
        Strength of regularization parameter for the ridge penalty.
    has_intercept: boolean 
        Is the first entry of coeffs an intercept parameter?

    Returns
    -------
    logistic_grad: ndarray, shape (n_features, )
        The computed gradient of the logistic cost.
    """
    p = predict_proba(X, coeffs)
    ridge_grad = 2 * coeffs
    if has_intercept:
        ridge_grad[0] = 0.0
    return np.dot(X.T, p - y) + lam * ridge_grad


def gradient_one_datapoint(x, y, coeffs):
    """
    Calculate the gradient of the logistic cost function evaluated at a single
    data point.

    Parameters
    ----------
    x: ndarray, shape (n_features, )
        The data (independent variables) to use for prediction.
    y: Integer, 0 or 1 
        The actual class values of the response.
    coeffs: ndarray, shape (n_features)
        The hypothosized coefficients of the logistic regression.

    Returns
    -------
    logistic_grad: ndarray, shape (n_features, )
        The computed gradient of the logistic cost.
    """
    linear_pred = np.sum(x * coeffs)
    p = 1 / (1 + np.exp(-linear_pred))
    return (x * (p - y))
