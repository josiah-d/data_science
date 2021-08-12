"""
Class implementing the CART decision tree algorithm.

"""

import pandas as pd
import numpy as np
import math
from collections import Counter
from TreeNode import TreeNode


class DecisionTree(object):
    """Classifier implementing the CART decision tree algorithm.

    Parameters
    ----------
    impurity_criterion: string, optional (default='entropy')
        String indicating the impurity_criterion to use.
        Use 'gini' to have tree us Gini impurity.
    """

    def __init__(self, impurity_criterion='entropy'):
        """Initialize an empty DecisionTree."""
        # Root Node
        self.root = None
        # String names of features (for interpreting the tree)
        self.feature_names = None
        # Boolean array of whether variable is categorical (or continuous)
        self.categorical = None

        if impurity_criterion == 'entropy':
            self.impurity_criterion = self._entropy
        else:
            self.impurity_criterion = self._gini


    def fit(self, X, y, feature_names=None):
        """Build the decision tree.

        Parameters
        ----------
        X: 2d numpy array, shape = [n_samples, n_features]
            The training data.
        y: 1d numpy array, shape = [n_samples]
            The training labels.
        feature_names: numpy array, optional (default=None)
            Array of strings containing names of each of the features.

        Returns
        -------
        None
        """
        if feature_names is None or len(feature_names) != X.shape[1]:
            self.feature_names = np.arange(X.shape[1])
        else:
            self.feature_names = feature_names

        # Create True/False array of whether the variable is categorical
        is_categorical = lambda x: isinstance(x, str) or isinstance(x, bool)
        self.categorical = np.vectorize(is_categorical)(X[0])

        self.root = self._build_tree(X, y)

    def _build_tree(self, X, y):
        """Recursively build the decision tree.

        Return the root node.

        Parameters
        ----------
        X: 2d numpy array, shape = [n_samples, n_features]
            The training data.
        y: 1d numpy array, shape = [n_samples]

        Returns
        -------
        TreeNode
        """
        node = TreeNode()
        index, value, splits = self._choose_split_index(X, y)

        if index is None or len(np.unique(y)) == 1:
            node.leaf = True
            node.classes = Counter(y)
            node.name = node.classes.most_common(1)[0][0]
        else:
            X1, y1, X2, y2 = splits
            node.column = index
            node.name = self.feature_names[index]
            node.value = value
            node.categorical = self.categorical[index]
            node.left = self._build_tree(X1, y1)
            node.right = self._build_tree(X2, y2)
        return node

    def _entropy(self, y):
        """Return the entropy of the array y.

        Parameters
        ----------
        y: 1d numpy array
            An array of data.

        Returns
        -------
        float
            Entropy of the array y.
        """
        n = y.shape[0]
        summation = 0
        for c_i in np.unique(y):
            prob = np.mean(y == c_i)
            summation += prob * np.log2(prob)
        return -summation

    def _gini(self, y):
        """Return the gini impurity of the array y.

        Parameters
        ----------
        y: 1d numpy array
            An array of data

        Returns
        -------
        float
            Gini impurity of the array y.
        """
        n = y.shape[0]
        summation = 0
        for c_i in np.unique(y):
            prob = np.mean(y == c_i)
            summation += prob**2
        return 1 - summation

    def _make_split(self, X, y, split_index, split_value):
        """Return the subsets of the dataset for the given split index & value.

        Call the method like this:
        >>> X1, y1, X2, y2 = self._make_split(X, y, split_index, split_value)

        Parameters
        ----------
        X: 2d numpy array
            Feature matrix.
        y: 1d numpy array
            Label matrix.
        split_index: int
            Index of the feature to split on.
        split_value: int/float/bool/str
            Value of feature to split on.

        Returns
        -------
        X1: 2d numpy array
            Feature matrix for subset 1
        y1: 1d numpy array
            Labels for subset 1
        X2: 2d numpy array
            Feature matrix for subset 2
        y2: 1d numpy array
            Labels for subset 2
        """
        if self.categorical[split_index]:
            idx = X[:, split_index] == split_value
        else:
            idx = X[:, split_index] < split_value
        return X[idx], y[idx], X[~idx], y[~idx]

    def _information_gain(self, y, y1, y2):
        """Return the information gain of making the given split.

        Use self.impurity_criterion(y) rather than calling _entropy or _gini
        directly.

        Parameters
        ----------
        y: 1d numpy array
            Labels for parent node.
        y1: 1d numpy array
            Labels for subset node 1.
        y2: 1d numpy array
            Labels for subset node 2.

        Returns
        -------
        float
            The information gain of making the given split.
        """
        n = y.shape[0]
        weighted_child_imp = 0
        for y_i in (y1, y2):
            weighted_child_imp += self.impurity_criterion(y_i) * y_i.shape[0] / n
        return self.impurity_criterion(y) - weighted_child_imp

    def _choose_split_index(self, X, y):
        """Return the index and value of the feature to split on.

        Determine which feature and value to split on. Return the index and
        value of the optimal split along with the split of the dataset.

        Return None, None, None if there is no split which improves information
        gain.

        Call the method like this:
        >>> index, value, splits = self._choose_split_index(X, y)
        >>> X1, y1, X2, y2 = splits

        Parameters
        ----------
            - X: 2d numpy array
            - y: 1d numpy array

        Returns
        -------
        index: int
            Index of feature
        value: int/float/bool/str
            Value of feature
        splits: tuple
            (2d array, 1d array, 2d array, 1d array)
        """
        split_index, split_value, splits = None, None, None
        best_gain = 0
        for i in range(X.shape[1]):
            values = np.unique(X[:, i])
            if len(values) <= 1:
                continue
            for value in values:
                X1, y1, X2, y2 = self._make_split(X, y, i, value)
                gain = self._information_gain(y, y1, y2)
                if gain > best_gain:
                    split_index = i
                    split_value = value
                    splits = (X1, y1, X2, y2)
                    best_gain = gain
        return split_index, split_value, splits

    def predict(self, X):
        """Return an array of predictions for the feature matrix X.

        Parameters
        ----------
        X: 2d numpy array
            The feature matrix.

        Returns
        -------
        y: 1d numpy array
            Matrix of predicted labels.
        """
        return np.array([self.root.predict_one(row) for row in X])

    def __str__(self):
        """Return string representation of the Decision Tree."""
        return str(self.root)
