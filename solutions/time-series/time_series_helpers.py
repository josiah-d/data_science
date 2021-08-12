from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import numpy as np

def reindex_to_data_frame(summary_series, df, freq):
    """Reindex a series of summary statistics to match the datetime index of
    a data frame.

    Parameters
    ----------
    summary_series: A pandas.Series of summary statistics created from a
        column in a dataframe.  For example, these could be monthly or annual
        means.

    df: A DataFrame.  The one used to construct summary_series.

    freq: A string frequency indicator.  Should match the frequency of the
        index to df.

    Returns
    -------
    reindexed_series: A Series containing the same information as
        summary_series, but reindexed to match the index of the data frame.

    Notes:
        NAs in the reindexing process are forward filled, so make sure that
    when the index of df represents date *intervals* (i.e. a monthly index)
    the left hand index is used.
    """
    min_date = df.index.min()
    resampled = summary_series.resample(freq).ffill()[min_date:]
    return resampled.reindex(df.index).ffill()


def to_col_vector(arr):
    """Convert a 1-dim numpy array into a column vector (i.e. an array with
    shape (n, 1).
    """
    return arr.reshape(-1, 1)


def plot_acf_and_pacf(series, axs, lags=24*2):
    """Plot the autocorrelation and partial autocorrelation plots of a series
    on a pair of axies.
    """
    _ = plot_acf(series, ax=axs[0], lags=lags)
    _ = plot_pacf(series, ax=axs[1], lags=lags)


class PolynomialBasisExpansion(object):

    def __init__(self, degree):
        """Create polynomial basis expansion features.

        Given a feature vector, this class generates a polynomial basis
        expansion of a given degree based on a standardized version of that
        feature.

        Parameters
        ----------
        degree: The degree of the polynomial basis expansion.

        Attributes
        ----------
        degree: The degree of the polynomial basis expansion.
        """
        self.degree = degree
        self._pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('basis', PolynomialFeatures(degree=degree))
        ])

    def fit(self, X):
        """Fit transformer to a training array.

        Memorizes the mean and standard deviation of the training array so
        future data can be standardized in the same way.

        Parameters
        ----------
        X: A numpy.array.

        Returns
        -------
        self: The current object.
        """
        if len(X.shape) == 1:
            X = to_col_vector(X)
        self._pipeline.fit(X)
        return self

    def transform(self, X):
        """Expand an array using a polynomail basis expansion.

        Parameters
        ----------
        X: A numpy.array to transform.

        Returns
        -------
        P: A numpy.array of shape (len(X), degree+1).  Each column is one
            feature in a polynomial basis expansion of the given degree of X.
        """
        if len(X.shape) == 1:
            X = to_col_vector(X)
        return self._pipeline.transform(X)

    def fit_transform(self, X):
        """Fit transformer to a training array, and return the transformed array.
        """
        return self.fit(X).transform(X)


class PolynomialBasisAndDummyizer(object):
    """Generate polynomial features and dummy variable features from a
    pandas.DataFrame.

    Parameters
    ----------
    poly_spec: A dictionary containing degree information for the polynomial
        features to be created.  Of the form {feature_name: degree}.

    dummy_list: A list of strings.  Feature names for features to dummyize.
    """

    def __init__(self, poly_spec=None, dummy_list=None):
        self.poly_spec = poly_spec
        self.dummy_list = dummy_list

        self._poly_expander = {}
        for feature, degree in poly_spec.items():
            self._poly_expander[feature] = PolynomialBasisExpansion(degree)

    def fit(self, df):
        """Fit the standardizations for the polynomial features.

        Parameters
        ----------
        df: A pandas.DataFrame.  Columns in this frame are used to fit the
            polynomial features.

        Returns
        -------
        self: The current object.
        """
        for feature in self.poly_spec:
            self._poly_expander[feature].fit(df[feature].values)
        return self

    def transform(self, df):
        """Expand columns from a dataframe into polynomial basis and dummy
        encoding expansions.

        Parameters
        ----------
        df: A pandas.DataFrame containing the features to transform.

        Returns
        -------
        X: A 2-dimensional numpy.array containing the new polynomial and
            dummy features.
        """
        feature_list = []
        for feature, transformer in self._poly_expander.items():
            feature_list.append(transformer.transform(df[feature].values))
        for feature in self.dummy_list:
            n_levels = df[feature].nunique()
            all_dummies = pd.get_dummies(df[feature], columns=[feature])
            # We strip the last column here to avoid identifiability issues in
            # regression.
            feature_list.append(all_dummies.ix[:, :(n_levels-1)])
        return np.column_stack(feature_list)

    def fit_transform(self, X):
        """Fit transformer to a training array, and return the transformed array.
        """
    def fit_transform(self, X):
        """Fit transformer to a training array, and return the transformed array.
        """
        return self.fit(X).transform(X)
