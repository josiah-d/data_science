#! /usr/bin/env python3
"""
This script reproduces all the images in the decision-rules assignment.

When updating this file, create the student version by replacing code
in the following functions and classes with a `pass` statement

    `plot_profit_curve`
    `profit_curve`
    `SMOTE`
    `plot_3`
    `do_sampling_study`
    `if __name__ == "__main__"`
    
This file can also be imported as a module and contains many different 
classes and functions:

Usage:
    python decision_rules.py

    Script must be run in the src/ directory, assuming the following 
    project directory structure:

        decision-rules/
        |----_data/
             |----churn.csv
        |----_images/
        |----_src/
             |----decision_rules.py

Authors:
    Kin-Yip Chien <kin-yip.chien@galvanize.com>
    Jack Bennetto <jack.bennetto@galvanize.com>

Functions And Classes:
    Profit Curves
    -------------
    load_churn : function
        Load and return the churn dataset (classification.)
    plot_profit_curve : function
        Plot expected profit curve for a classifier.
    plot_profit_curve_v2 : function
        Plot expected profit curve for a classifier with more options.
    plot_toy_profit_curve : function
        Plot expected profit curve for toy example.
    profit_curve : function
        Calculate expected profits and thresholds.
    standard_confusion_matrix : function
        Compute a confusion matrix of the format:
            -----------
            | TP | FP |
            -----------
            | FN | TN |
            -----------

    Sampling Methods For Imbalanced Data
    ------------------------------------
    Oversample : class
        Class for oversampling the minority class at random.
    SMOTE : class
        Class for implementing SMOTE.
    SMOTE_v2 : class
        Class for optimized implementation of SMOTE.
    Undersample : class
        Class for undersampling the majority class at random.
    NearestNeighbor : class
        Class for implementing neighbor searches.
    check_array : function
        Checks if input is a 2D array.
    check_is_fitted : function
        Checks if the estimator is fitted.
    check_mnr_mjr_ratio : function
        Validates the minority to majority ratio.
    check_n_neighbors : function
        Validates number of neighbors.
    class_summary : function
        Summarizes minority and majority class information from data.
    distance_matrix : function
        Compute the distance matrix.
    euclidean : function
        Compute the row-wise Euclidean distance(s) between two arrays.

    Plot Assignment Figures
    -----------------------
    plot_1 : function 
        Plot expected profits per customer for toy classifier with 
        `plot_toy_profit_curve`.
    plot_2 : function
        Plot expected profits per customer with for toy classifier with 
        matplotlib step plot function.
    plot_3 : function
        Plot profit curve for logistic regression fit to churn data 
        with `plot_profit_curve`.
    plot_4 : function 
        Plot profit curve for several models with 
        `plot_profit_curve_v2`.
    plot_5 : function
        Plot the effect of different sampling methods on a 
        classifier's decision boundary.
        
    Sampling Study
    --------------
    do_sampling_study : function
        Study the effect of different sampling methods on 
        expected profit using the churn dataset.
"""
from math import inf
import matplotlib.pyplot as plt
from numbers import Integral
import numpy as np
from numpy.random import default_rng
import pandas as pd
from pathlib import Path
from sklearn.metrics import confusion_matrix
# For profit curve plot_n functions.
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier as GBC
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
# For imbalanced dataset plot_n functions.
from collections import Counter
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_classification
# For sampling methods study.
from sklearn.pipeline import Pipeline


def load_churn(filepath='../data/churn.csv', *, return_X_y=False, 
               as_frame=False):
    """
    Load and return the churn dataset (classification.)
    
    Telco customer data circa 1998.
    
    Follows `sklearn.datasets` dataset loaders API.
    
    =================   ==============
    Classes                          2
    Samples per class      [2850, 483]
    Samples total                 3333
    Dimensionality                  20
    Features                     mixed
    =================   ==============
    
    Parameters
    ----------
    filepath : str, default='../data/churn.csv'
        Path of churn.csv.
    return_X_y : bool, default=False
        If True, returns ``(data, target)`` instead of a 
        dictionary object.
        See below for more information about the 
        `data` and `target` object.
    as_frame : bool, default=False
        If True, the data is a pandas DataFrame including columns with 
        appropriate dtypes. The target is a pandas DataFrame or Series 
        depending on the number of target columns.
        If `return_X_y` is True, then (`data`, `target`) will be 
        pandas DataFrames or Series as described below.
    
    Returns
    -------
    data : dict
        dictionary object, with the following items.
        
        data : {ndarray, dataframe} of shape (3333, 20)
            The data matrix. If `as_frame=True`, `data` will be a 
            pandas DataFrame.
        target: {ndarray, Series} of shape (3333,)
            The classification target. If `as_frame=True`, 
            `target` will be a pandas Series.
        feature_names: list
            The names of the dataset columns.
        frame: DataFrame of shape (3333, 21)
            Only present when `as_frame=True`. DataFrame with 
            `data` and `target`.
            
    (data, target) : tuple if `return_X_y` is True
    
    Examples
    --------
    >>> X, y = load_churn(return_X_y=True)
    >>> print(X.shape)
    (3333, 20)
    """
    filename = Path(filepath)
    df = pd.read_csv(filename).replace(
        {'no': 0, 'yes': 1, 'False.': 0, 'True.': 1})
    
    frame = None
    if as_frame:
        frame = df.copy()
        target = df.pop('Churn?')
        data = df
    else:
        target = df.pop('Churn?').to_numpy()
        data = df.to_numpy()
        
    if return_X_y:
        return data, target
    feature_names = df.columns
    return {'data': data, 'target': target, 'frame': frame, 
            'feature_names': feature_names, 
            'filename': str(filename.resolve())}


def plot_profit_curve(model, profit_mat, X, y):
    """
    Plot expected profit curve for a classifier.

    For demonstrating assignment only. Use `plot_profit_curve_v2` for 
    analysis as it has more options.

    Parameters
    ----------
    model : estimator instance
        Fitted classifier or a fitted pipeline in which the 
        last estimator is a classifier.
    profit_mat : array-like of shape (2, 2)
        Profit matrix with payoffs corresponding to:
            -----------
            | TP | FP |
            -----------
            | FN | TN |
            -----------        
    X : array-like of shape (n_samples, n_features)
        Input values.
    y : array-like of shape (n_samples,)
        Binary target values.
        
    Returns
    -------
    None
        
    See Also
    --------
    plot_profit_curve_v2 : Plot expected profit curve for a classifier 
        with more options.
        
    Examples
    --------
    >>> from matplotlib import pyplot  # doctest: +SKIP
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.metrics import plot_confusion_matrix
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.svm import SVC
    >>> X, y = make_classification(random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(
    ...     X, y, random_state=0)
    >>> clf = SVC(probability=True, random_state=0)
    >>> clf.fit(X_train, y_train)
    SVC(probability=True, random_state=0)
    >>> profit_mat = [[3, -1], [0, 0]]
    >>> plot_profit_curve(clf, profit_mat, 
    ...                   X_test, y_test)  # doctest: +SKIP
    >>> pyplot.show()  # doctest: +SKIP
    """
    # Predict probabilities of being the positive class.
    y_probs = model.predict_proba(X)[:, 1]
    exp_profits, thresholds = profit_curve(y, y_probs, profit_mat)
    
    pcts = np.linspace(0, 100, len(thresholds))
    plt.figure(figsize=(8.5, 4), tight_layout=True)
    plt.step(pcts, exp_profits, 'k', where='post', 
            label=model.__class__.__name__)
    plt.title('Profits of Classifiers')
    plt.xlabel('Percentage Of Test Instances (Decreasing By Score)')
    plt.ylabel('Profit')
    plt.legend()


def plot_profit_curve_v2(model, profit_mat, X, y, 
                         per_instance=False, ax=None):
    """
    Plot expected profit curve for a classifier.
    
    Has more options than `plot_profit_curve`.
    
    Parameters
    ----------
    model : estimator instance
        Fitted classifier or a fitted pipeline in which the 
        last estimator is a classifier.
    profit_mat : array-like of shape (2, 2)
        Profit matrix with payoffs corresponding to:
            -----------
            | TP | FP |
            -----------
            | FN | TN |
            -----------        
    X : array-like of shape (n_samples, n_features)
        Input values.
    y : array-like of shape (n_samples,)
        Binary target values.
    per_instance : bool, default=False
        Whether to calculate profit per instance or total profit.
    ax : matplotlib axes, default=None
        Axes object to plot on. If `None`, a new figure and axes 
        is created.
        
    Returns
    -------
    fig : matplotlib figure
        Figure containing the curve.
    ax : matplotlib axes
        Axes with profit curve.
    lines : matplotlib Line2D
        A list of Line2D objects representing the profit curve.
        
    Examples
    --------
    >>> from matplotlib import pyplot  # doctest: +SKIP
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.metrics import plot_confusion_matrix
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.svm import SVC
    >>> X, y = make_classification(random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(
    ...     X, y, random_state=0)
    >>> clf = SVC(probability=True, random_state=0)
    >>> clf.fit(X_train, y_train)
    SVC(probability=True, random_state=0)
    >>> profit_mat = [[3, -1], [0, 0]]
    >>> plot_profit_curve_v2(clf, profit_mat, 
    ...                      X_test, y_test)  # doctest: +SKIP
    >>> pyplot.show()  # doctest: +SKIP        
    """
    # Predict probabilities of being the positive class.
    y_probs = model.predict_proba(X)[:, 1]
    exp_profits, thresholds = profit_curve(y, y_probs, profit_mat, 
                                           per_instance)
    
    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(16, 9), tight_layout=True)
        
    ylabel = 'Profit'
    if per_instance:
        x = thresholds
        xlabel = 'Classification Threshold'
        ylabel += ' Per Customer'
        ax.set_xlim(1.05, -0.05)
    else:
        pcts = np.linspace(0, 100, len(thresholds))
        x = pcts
        xlabel = 'Percentage Of Test Instances (Decreasing By Score)'
        
    if model.__class__.__name__ == 'Pipeline':
        label = model['clf'].__class__.__name__
    else:
        label = model.__class__.__name__
    lines = ax.step(x, exp_profits, where='post', 
                    label=label)
    
    ax.set(title='Profits Of Classifiers', 
           xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    
    return fig, ax, lines


def plot_toy_profit_curve(y_true, y_probs, profit_mat, 
                          per_instance=False, ax=None, annotate=False):
    """
    Plot expected profit curve for toy example.
    
    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True binary labels ({0, 1}.)
    y_probs : array-like of shape (n_samples,)
        Predicted probabilities of the positive class.
    profit_mat : array-like of shape (2, 2)
        Profit matrix with payoffs corresponding to:
            -----------
            | TP | FP |
            -----------
            | FN | TN |
            -----------
    per_instance : bool, default=False
        Whether to calculate profit per instance or total profit.
    ax : matplotlib axes, default=None
        Axes object to plot on. If `None`, a new figure and axes 
        is created.
    annotate : bool, default=False
        Whether to annotate profit values on curve.
        
    Returns
    -------
    fig : matplotlib figure
        Figure containing the profit curve.
    ax : matplotlib axes
        Axes with profit curve.
        
    Examples
    --------
    >>> from matplotlib import pyplot  # doctest: +SKIP
    >>> y_labels = [0, 0, 1]
    >>> y_probs = [0.2, 0.6, 0.4]
    >>> profit_mat = [[3, -1], [0, 0]]
    >>> plot_toy_profit_curve(y_labels, y_probs, 
    ...                       profit_mat)  # doctest: +SKIP
    >>> pyplot.show()  # doctest: +SKIP
    """
    exp_profits, thresholds = profit_curve(y_true, y_probs, 
                                           profit_mat, per_instance)
    
    # Order points from lowest to highest threshold.
    exp_profits = exp_profits[::-1]
    thresholds = thresholds[::-1]
    if 0 not in thresholds:
        # Add a threshold at 0 for plotting.
        thresholds = np.append(0, thresholds)
        # Repeat the expected profit for threshold 1 for plotting.
        exp_profits = np.append(exp_profits, exp_profits[-1])
        
    # Plot profit curve.
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4.5), tight_layout=True)
    for i in range(len(thresholds) - 1):
        if i == 0:
            # Close the left endpoint of the threshold interval when 
            # the threshold is 0.
            ax.plot(thresholds[i], exp_profits[i], 'ko')
        else:
            # Open the left endpoint of the threshold interval.
            ax.plot(thresholds[i], exp_profits[i], 'ko', mfc='None')
        # Plot a segment over threshold intervals that yield the same 
        # expected profit.
        ax.plot(thresholds[i : i + 2], exp_profits[[i, i]], 'k')
        # Close the right endpoint of the interval.
        ax.plot(thresholds[i + 1], exp_profits[i], 'ko')
        
        if annotate:
            ax.annotate(f'{exp_profits[i]:.2f}', 
                        (thresholds[i], exp_profits[i]), 
                        xytext=(4, 0), 
                        textcoords='offset points',
                        va='center')
            
    ylabel = 'Profit'
    if per_instance:
        ylabel += ' Per Customer'
        
    ax.set(title='Profits',
           xlabel='Classification Threshold',
           xlim=(1.05, -0.05), # Reverse x-axis.
           ylabel=ylabel)
    
    return fig, ax


def profit_curve(y_true, y_probs, profit_mat, per_instance=False):
    """
    Calculate expected profits for classification thresholds based on 
    true binary labels, predicted probabilities of the positive class 
    and a profit matrix.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True binary labels ({0, 1}.)
    y_probs : array-like of shape (n_samples,)
        Predicted probabilities of the positive class.
    profit_mat : array-like of shape (2, 2)
        Profit matrix with payoffs corresponding to:
            -----------
            | TP | FP |
            -----------
            | FN | TN |
            -----------
    per_instance : bool, default=False
        Whether to calculate total profit or profit per instance.
            
    Returns
    -------
    exp_profits : ndarray of shape (n_thresholds,)
        Expected profits for every classification threshold.
    thresholds : ndarray of shape (n_thresholds,)
        Classification thresholds in decreasing order. Not unique.
        
    Examples
    --------
    >>> y_true = [0, 0, 1]
    >>> y_probs = [0.2, 0.6, 0.4]
    >>> profit_mat = [[3, -1], [0, 0]]
    >>> profit_curve(
    ...     y_true, y_probs, profit_mat, per_instance=True)
    (array([ 0.        , -0.33333333,  0.66666667,  0.33333333]), array([1. , 0.6, 0.4, 0.2]))
    """
    # Consider all thresholds including 1.
    if 1 not in y_probs:
        y_probs = np.append(y_probs, [1])
    
    thresholds = np.sort(y_probs)[::-1]
    
    exp_profits = np.empty(thresholds.shape)
    for i, threshold in enumerate(thresholds):
        # Predicted labels for a given threshold.
        y_pred = y_probs >= threshold
        conf_mat = standard_confusion_matrix(y_true, y_pred)
        exp_profits[i] = (conf_mat * profit_mat).sum()
        
    if per_instance:
        exp_profits /= len(y_true)
        
    return exp_profits, thresholds


def standard_confusion_matrix(y_true, y_pred, sklearn=False):
    """
    Compute a confusion matrix of the format:
        -----------
        | TP | FP |
        -----------
        | FN | TN |
        -----------
                  
    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True binary labels ({0, 1}.)
    y_pred : array-like of shape (n_samples,)
        Predicted binary labels ({0, 1}.)
    sklearn : bool, default=False
        Implement function by unpacking tuple from 
        `sklearn.metrics.confusion_matrix` return.

    Returns
    -------
    conf_mat : ndarray of shape (2, 2)
    
    Examples
    --------
    >>> y_true = [1, 1, 1, 1, 1, 0, 0]
    >>> y_pred = [1, 1, 1, 1, 0, 0, 0]
    >>> standard_confusion_matrix(y_true, y_pred)
    array([[4, 0],
           [1, 2]])
    """
    if sklearn:
        [[tn, fp], [fn, tp]] = confusion_matrix(y_true, y_pred)
    else:
        tp, fp, fn, tn = 0, 0, 0, 0
        for tup in zip(y_true, y_pred):
            if tup == (1, 1):
                tp += 1
            elif tup == (0, 1):
                fp += 1
            elif tup == (1, 0):
                fn += 1
            else:
                tn += 1
    return np.array([[tp, fp], [fn, tn]])


class Oversample:
    """
    Class for oversampling the minority class by picking samples at 
    random.
    
    Duplicate sets of minority class observations to reach a desired 
    ratio of minority class observations to majority class 
    observations. For example, if there are 10 minority class 
    instances and 103 majority class instances, oversampling would 
    copy the 10 minority instances 9 times each and sample an 
    additional 3 minority instances without replacement.

    Only handles two classes.

    Parameters
    ----------
    mnr_mjr_ratio : float, default=1.0
        Desired ratio of majority class observations to 
        minority class observations; must be a positive float.
    random_state : int or None, default=None
        Determines random number generation for dataset creation. Pass 
        an int for reproducible output across multiple function calls.
        
    Attributes
    ----------
    sample_indices_ : ndarray of shape (n_new_samples,)
        Indices of the samples selected.
    """
    
    def __init__(self, *, mnr_mjr_ratio=1.0, random_state=None):
        self.mnr_mjr_ratio = mnr_mjr_ratio
        self.random_state = random_state
        self.method = 'oversample'

    def __repr__(self):
        attrs = ['mnr_mjr_ratio', 'random_state']
        defaults = [1, None]
        current = [getattr(self, attr) for attr in attrs]
        show = np.asarray(current) != defaults
        display = np.array([f'mnr_mjr_ratio={self.mnr_mjr_ratio}', 
                            f'random_state={self.random_state}'])
        return f"{type(self).__name__}({', '.join(display[show])})"

    def fit_resample(self, X, y):
        """
        Oversample the data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Matrix containing the data which have to be sampled.
        y : array-like of shape (n_samples,)
            Corresponding label for each sample in X.

        Returns
        -------
        X_oversampled : ndarray of shape (n_oversamples, n_features)
            The array containing oversampled data.
        y_oversampled : ndarray of shape (n_oversamples,)
            The corresponding labels of `X_oversampled`.

        Examples
        --------
        >>> from collections import Counter
        >>> from sklearn.datasets import make_classification
        >>> X, y = make_classification(
        ...     n_samples=1000, n_informative=3, n_redundant=1, 
        ...     n_clusters_per_class=1, weights=[0.1, 0.9], flip_y=0, 
        ...     class_sep=2, random_state=10)
        >>> print(f'Original dataset shape {Counter(y)}')
        Original dataset shape Counter({1: 900, 0: 100})
        >>> over = Oversample(random_state=42)
        >>> X_over, y_over = over.fit_resample(X, y)
        >>> print(f'Oversampled dataset shape {Counter(y_over)}')
        Oversampled dataset shape Counter({0: 900, 1: 900})
        """
        rng = default_rng(self.random_state)
        res = class_summary(X, y)
        X_c = res['data']
        y_c = res['target']
        mjr_label, mnr_label = res['labels']
        mjr_cnt, mnr_cnt = res['counts']
        mjr_idx, mnr_idx = res['indices']
        mnr_mjr_ratio = check_mnr_mjr_ratio(
            self.mnr_mjr_ratio, mnr_cnt, mjr_cnt, self.method)
        
        # Calculate minority class oversample size to attain desired 
        # minority to majority ratio.    
        n_oversamples = mnr_mjr_ratio * mjr_cnt
        # Duplicate full sets of minority class observations before 
        # randomly selecting minority class observations to obtain the 
        # oversample size.
        repeats = n_oversamples // mnr_cnt
        remainder = round(n_oversamples - repeats*mnr_cnt)
        rng.shuffle(mnr_idx)
        self.sample_indices_ = np.concatenate(
            (np.repeat(mnr_idx, repeats), mnr_idx[:remainder]))
        keep = np.append(self.sample_indices_, mjr_idx)

        # Return oversampled X, y.
        X_oversampled, y_oversampled = X_c[keep], y_c[keep]
        return X_oversampled, y_oversampled

    
class SMOTE:
    """
    Class for implementing SMOTE: Synthetic Minority Over-sampling 
    TEchnique as presented in [1]_.
    
    Parameters
    ----------
    T : int
        Number of minority class samples.
    N : int or float
        Amount of SMOTE N%.
    k : int, default = 5
        Number of nearest neighbors.
    random_state : int or None, default=None
        Determines random number generation for dataset creation. Pass 
        an int for reproducible output across multiple function calls.
        
    Attributes
    ----------
    numattrs : int
        Number of attributes
    sample : ndarray of shape (T, numattrs)
        Original minority class samples.
    newindex : int
        Number of synthetic samples generated.
    synthetic: ndarray of shape (newindex, numattrs)
        Synthetic samples.
        
    References
    ----------
    .. [1] N. V. Chawla, K. W. Bowyer, L. O.Hall, W. P. Kegelmeyer, 
       "SMOTE: synthetic minority over-sampling technique," Journal of 
       artificial intelligence research, 321-357, 2002.
    """
    
    def __init__(self, T, N, k=5, random_state=None):
        self.rng = default_rng(random_state)
        # If N is less than 100%, randomize the minority class samples 
        # as only a random percent of them will be SMOTEd.
        if N < 100:
            self.rng.shuffle(X)
            T = (N / 100) * T
            N = 100
        self.T = T
        # The amount of SMOTE is assumed to be in 
        # integral multiples of 100.
        self.N = int(N / 100)
        self.k = k
        self.newindex = 0
        self.synthetic = []
        
    def fit_resample(self, X):
        """
        SMOTE the samples.
        
        Parameters
        ----------
        X : ndarray of shape (T, numattrs)
            Minority class samples.
            
        Returns
        -------
        synthetic : ndarray of shape (newindex, numattrs)
            Synthetic samples.
            
        Examples
        --------
        >>> from collections import Counter
        >>> from numpy import append, vstack, zeros
        >>> from sklearn.datasets import make_classification
        >>> X, y = make_classification(
        ...     n_samples=1000, n_informative=3, n_redundant=1, 
        ...     n_clusters_per_class=1, weights=[0.1, 0.9], flip_y=0, 
        ...     class_sep=2, random_state=10)
        >>> print('Original dataset shape %s' % Counter(y))
        Original dataset shape Counter({1: 900, 0: 100})
        >>> T, N, mnr_label = 100, 800, 0
        >>> sm = SMOTE(T, N, random_state=42)
        >>> y_sm = append(y, zeros(N, dtype=int))
        >>> X_sm = sm.fit_resample(X[y == mnr_label])
        >>> X_sm = vstack((X, X_sm))
        >>> print('SMOTEd dataset shape %s' % Counter(y_sm))
        SMOTEd dataset shape Counter({0: 900, 1: 900})
        """
        self.numattrs = X.shape[1]
        self.sample = X
        for i in range(self.T):
            nbrs = NearestNeighbors(n_neighbors=self.k)
            nbrs.fit(self.sample)
            nnarray = nbrs.kneighbors(self.sample[i].reshape(1, -1), 
                                      return_distance=False).reshape(-1,)
            self._populate(self.N, i, nnarray)
        return np.asarray(self.synthetic)
    
    def _populate(self, N, i, nnarray):
        """
        Generates synthetic samples.
        
        The synthetic instance is created by choosing one of the *k* 
        nearest neighbors of *a* at random (call it *b*) and 
        connecting *a* and *b* to form a line segment in the 
        feature space, and then picking a point randomly along that 
        line (ie. a convex combination of the two chosen instances 
        *a* and *b*.)
        
        Parameters
        ----------
        N : int
            Number of nearest neighbors to choose to achieve 
            over-sampling amount.
        i : int
            Index of original minority class samples.
        nnarray : ndarray of shape (n_neighbors,)
            Indices of nearest neighbors for 
            original minority class sample i.
        
        Returns
        -------
        None
        """
        while N != 0:
            # Choose one of the k nearest neighbors of i.
            nn = self.rng.choice(self.k)
            new = []
            gap = self.rng.random()
            for attr in range(self.numattrs):
                dif = self.sample[nnarray[nn]][attr] - self.sample[i][attr]
                new.append(self.sample[i][attr] + gap * dif)
            self.synthetic.append(new)
            self.newindex += 1
            N -= 1
            

class SMOTE_v2:
    """
    Class for optimized implementation of SMOTE: Synthetic Minority 
    Over-sampling TEchnique based on [1]_.
    
    SMOTE first selects a minority class instance (call it *a*) at 
    random and finds its *k* nearest minority class neighbors. The 
    synthetic instance is then created by choosing one of the 
    *k* nearest neighbors (call it *b*) at random and 
    connecting *a* and *b* to form a line segment in the 
    feature space, and then picking a point randomly along that line 
    (ie. a convex combination of the two chosen instances *a* and *b*.)

    Depending upon the amount of over-sampling required, neighbors 
    from the k nearest neighbors are randomly chosen. For instance, 
    if the amount of over-sampling needed is 200%, only 
    two neighbors from the five nearest neighbors are chosen and 
    one sample is generated in the direction of each.

    Parameters
    ----------
    mnr_mjr_ratio : float, default=1.0
        Desired ratio of majority class observations to 
        minority class observations; must be a positive float.
    k : int, default = 5
        Number of nearest neighbors.
    random_state : int or None, default=None
        Determines random number generation for dataset creation. Pass 
        an int for reproducible output across multiple function calls.
        
    Attributes
    ----------
    sample_indices_ : ndarray of shape (n_new_samples,)
        Indices of the samples selected.
        
    References
    ----------
    .. [1] N. V. Chawla, K. W. Bowyer, L. O.Hall, W. P. Kegelmeyer, 
       "SMOTE: synthetic minority over-sampling technique," Journal of 
       artificial intelligence research, 321-357, 2002.
    """
    
    def __init__(self, *, mnr_mjr_ratio=1.0, k=5, random_state=None):
        self.mnr_mjr_ratio = mnr_mjr_ratio
        self.k = k
        self.random_state = random_state
        self.method = 'oversample'

    def __repr__(self):
        attrs = ['mnr_mjr_ratio', 'k', 'random_state']
        defaults = [1, 5, None]
        current = [getattr(self, attr) for attr in attrs]
        show = np.asarray(current) != defaults
        display = np.array([f'mnr_mjr_ratio={self.mnr_mjr_ratio}', 
                            f'k={self.k}', 
                            f'random_state={self.random_state}'])
        return f"{type(self).__name__}({', '.join(display[show])})"

    def fit_resample(self, X, y):
        """
        SMOTE the data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Matrix containing the data which have to be sampled.
        y : array-like of shape (n_samples,)
            Corresponding label for each sample in X.

        Returns
        -------
        X_smoted : ndarray of shape (n_smote, n_features)
            The array containing SMOTEd data.
        y_smoted : ndarray of shape (n_smote,)
            The corresponding labels of `X_smote`.

        Examples
        --------
        >>> from collections import Counter
        >>> from sklearn.datasets import make_classification
        >>> X, y = make_classification(
        ...     n_samples=1000, n_informative=3, n_redundant=1, 
        ...     n_clusters_per_class=1, weights=[0.1, 0.9], flip_y=0, 
        ...     class_sep=2, random_state=10)
        >>> print(f'Original dataset shape {Counter(y)}')
        Original dataset shape Counter({1: 900, 0: 100})
        >>> smote = SMOTE_v2(random_state=42)
        >>> X_smote, y_smote = smote.fit_resample(X, y)
        >>> print(f'SMOTEd dataset shape {Counter(y_smote)}')
        SMOTEd dataset shape Counter({0: 900, 1: 900})
        """
        self.rng = default_rng(self.random_state)
        res = class_summary(X, y)
        X_c = res['data']
        y_c = res['target']
        mjr_label, mnr_label = res['labels']
        mjr_cnt, mnr_cnt = res['counts']
        mjr_idx, mnr_idx = res['indices']
        mnr_mjr_ratio = check_mnr_mjr_ratio(
            self.mnr_mjr_ratio, mnr_cnt, mjr_cnt, self.method)
        
        # Calculate number of synthentic samples to generate to attain 
        # desired minority to majority ratio.
        n_total = round(mnr_mjr_ratio * mjr_cnt)
        n_smote = n_total - mnr_cnt
        self.new_i = 0
        # Array for synthetic samples
        self.synthetic = np.empty((n_smote, X_c.shape[1]))
        # Array for original minority class samples.
        self.X_mnr = X_c[mnr_idx]

        # Randomize the minority class samples.
        self.rng.shuffle(self.X_mnr, axis=0)
        # Compute the k nearest neighbors for each sample, and save the 
        # indices as rows in nnarrays.
        nbrs = NearestNeighbors(n_neighbors=self.k).fit(self.X_mnr)
        nnarrays = nbrs.kneighbors(return_distance=False)
        # Randomize the order of neighbors.
        for row in nnarrays:
            self.rng.shuffle(row)

        self.n_passes = n_smote // mnr_cnt
        self.neighbors = np.arange(self.k)
        if self.n_passes > 0:
            for i in range(mnr_cnt):
                self._populate(self.n_passes, i, nnarrays[i])

        smote_remain = n_smote - self.n_passes*mnr_cnt
        if smote_remain > 0:
            self.n_passes = 1
            for i in range(smote_remain):
                self._populate(self.n_passes, i, nnarrays[i])

        self.sample_indices_ = np.arange(n_total)[len(y_c):]
        # Return SMOTEd X, y
        X_smoted = np.vstack((X_c, self.synthetic))
        y_smoted = np.append(y_c, np.repeat(mnr_label, n_smote))
        return X_smoted, y_smoted
            
    def _populate(self, N, i, nnarray):
        """
        Generates synthetic samples.
        
        The synthetic instance is created by choosing one of the *k* 
        nearest neighbors of *a* at random (call it *b*) and 
        connecting *a* and *b* to form a line segment in the 
        feature space, and then picking a point randomly along that 
        line (ie. a convex combination of the two chosen instances 
        *a* and *b*.)
        
        Parameters
        ----------
        N : int
            Number of nearest neighbors to choose to achieve 
            over-sampling amount.
        i : int
            Index of original minority class samples.
        nnarray : ndarray of shape (n_neighbors,)
            Indices of nearest neighbors for 
            original minority class sample i.
        
        Returns
        -------
        None
        """
        nn = []
        while N != 0:
            # Choose as many of the k nearest neighbors of i as 
            # possible to quickly generate samples.
            n_select = int(min(N, self.k))
            nn.extend(self.neighbors[:n_select])
            N -= n_select
        dif = self.X_mnr[nnarray[nn]] - self.X_mnr[i]
        # Random number between 0 and 1 for each neighbor selected.
        gap = self.rng.random((self.n_passes, 1))
        syn = self.X_mnr[i] + gap * dif
        self.synthetic[self.new_i : self.new_i + self.n_passes] = syn
        self.new_i += self.n_passes

        
class Undersample:
    """
    Class for undersampling the majority class by 
    picking samples at random.
    
    Discard majority class observations at random to reach a desired 
    ratio of minority class observations to majority class 
    observations.
    
    Only handles two classes.

    Parameters
    ----------
    mnr_mjr_ratio : float, default=1.0
        Desired ratio of majority class observations to 
        minority class observations; must be a positive float.
    random_state : int or None, default=None
        Determines random number generation for dataset creation. Pass 
        an int for reproducible output across multiple function calls.
        
    Attributes
    ----------
    sample_indices_ : ndarray of shape (n_new_samples,)
        Indices of the samples selected.
    """
    
    def __init__(self, *, mnr_mjr_ratio=1.0, random_state=None):
        self.mnr_mjr_ratio = mnr_mjr_ratio
        self.random_state = random_state
        self.method = 'undersample'

    def __repr__(self):
        attrs = ['mnr_mjr_ratio', 'random_state']
        defaults = [1, None]
        current = [getattr(self, attr) for attr in attrs]
        show = np.asarray(current) != defaults
        display = np.array([f'mnr_mjr_ratio={self.mnr_mjr_ratio}', 
                            f'random_state={self.random_state}'])
        return f"{type(self).__name__}({', '.join(display[show])})"

    def fit_resample(self, X, y):
        """
        Undersample the data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Matrix containing the data which have to be sampled.
        y : array-like of shape (n_samples,)
            Corresponding label for each sample in X.

        Returns
        -------
        X_undersampled : ndarray of shape (n_undersamples, n_features)
            The array containing undersampled data.
        y_undersampled : ndarray of shape (n_undersamples,)
            The corresponding labels of `X_undersampled`.

        Examples
        --------
        >>> from collections import Counter
        >>> from sklearn.datasets import make_classification
        >>> X, y = make_classification(
        ...     n_samples=1000, n_informative=3, n_redundant=1, 
        ...     n_clusters_per_class=1, weights=[0.1, 0.9], flip_y=0, 
        ...     class_sep=2, random_state=10)
        >>> print(f'Original dataset shape {Counter(y)}')
        Original dataset shape Counter({1: 900, 0: 100})
        >>> undr = Undersample(random_state=42)
        >>> X_undr, y_undr = undr.fit_resample(X, y)
        >>> print(f'Undersampled dataset shape {Counter(y_undr)}')
        Undersampled dataset shape Counter({0: 100, 1: 100})
        """
        rng = default_rng(self.random_state)
        res = class_summary(X, y)
        X_c = res['data']
        y_c = res['target']
        mjr_label, mnr_label = res['labels']
        mjr_cnt, mnr_cnt = res['counts']
        mjr_idx, mnr_idx = res['indices']
        mnr_mjr_ratio = check_mnr_mjr_ratio(
            self.mnr_mjr_ratio, mnr_cnt, mjr_cnt, self.method)
        
        # Calculate how many majority class observations to keep to 
        # attain desired minority to majority ratio.
        n_undr = round(mnr_cnt / mnr_mjr_ratio)
        # Randomly discard majority class observations.
        idx = np.arange(len(y_c))
        rng.shuffle(mjr_idx)
        drop = mjr_idx[n_undr:]
        self.sample_indices_ = mjr_idx[:n_undr]
        keep = np.isin(idx, drop, assume_unique=True, invert=True)
    
        # Return undersampled X, y.
        X_undersampled, y_undersampled = X_c[keep], y_c[keep] 
        return X_undersampled, y_undersampled
    
    
class NearestNeighbors:
    """
    Class for implementing neighbor searches.
    
    Mimics `sklearn.neighbors.NearestNeighbors`.
    
    Parameters
    ----------
    n_neighbors : int, default=5
        Number of neighbors to use by default for :meth:`kneighbors` queries.
    metric : str, default='euclidean'
        The distance metric to use.

    Attributes
    ----------
    metric_ : str
        Metric used to compute distances to neighbors.
    n_samples_fit_ : int
        Number of samples in the fitted data.
    
    Examples
    --------
    >>> samples = [[0, 0, 2], [1, 0, 0], [0, 0, 1]]
    >>> neigh = NearestNeighbors(n_neighbors=2)
    >>> neigh.fit(samples)
    NearestNeighbors(n_neighbors=2)
    >>> neigh.kneighbors([[0, 0, 1.3]], 2, return_distance=False)
    array([[2, 0]], dtype=int64)
    """
    
    def __init__(self, *, n_neighbors=5, metric='euclidean'):
        self.n_neighbors = n_neighbors
        self.metric = metric
            
    def __repr__(self):
        attrs = ['n_neighbors']
        defaults = [5]
        current = [getattr(self, attr) for attr in attrs]
        show = np.asarray(current) != defaults
        display = np.array([f'n_neighbors={self.n_neighbors}'])
        return f"{type(self).__name__}({', '.join(display[show])})"

    def fit(self, X, y=None):
        """
        Fit the nearest neighbors estimator from the training dataset.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data.
            
        y : Ignored
            Not used, present for API consistency by convention.
            
        Returns
        -------
        self : NearestNeighbors
            The fitted nearest neighbors estimator.
        """
        if self.metric != 'euclidean':
            raise NotImplementedError("NearestNeighbors only supports "
                                      "metric='euclidean'.")
        self.metric_ = self.metric
        check_n_neighbors(self.n_neighbors)
        self._fit_X = check_array(X)
        self.n_samples_fit_ = len(X)
        return self
    
    def kneighbors(self, X=None, n_neighbors=None, 
                   return_distance=True):
        """
        Finds the k-neighbors of a point.
        
        Returns indices and distances to the neighbors of each point.
        
        Parameters
        ----------
        X : array-like of shape (n_queries, n_features)
            The query point or points. If not provided, neighbors of 
            each indexed point are returned. In this case, the 
            query point is not considered its own neighbor.
        n_neighbors : int, default=None
            Number of neighbors required for each sample. The default 
            is the value passed to the constructor.
        return_distance : bool, default=True
            Whether or not to return the distances.

        Returns
        -------
        neigh_dist : ndarray of shape (n_queries, n_neighbors)
            Array representing the lengths to points, only present if
            `return_distance=True`.
        neigh_ind : ndarray of shape (n_queries, n_neighbors)
            Indices of the nearest points in the population matrix.

        Examples
        --------
        In the following example, we construct a NearestNeighbors
        class from an array representing our data set and ask who's
        the closest point to [1,1,1]
        >>> samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]
        >>> neigh = NearestNeighbors(n_neighbors=1)
        >>> neigh.fit(samples)
        NearestNeighbors(n_neighbors=1)
        >>> neigh.kneighbors([[1., 1., 1.]])
        (array([[0.5]]), array([[2]], dtype=int64))
        
        As you can see, it returns [[0.5]], and [[2]], which means 
        that the element is at distance 0.5 and is the third element 
        of samples (indexes start at 0). You can also query for 
        multiple points:
        >>> X = [[0., 1., 0.], [1., 0., 1.]]
        >>> neigh.kneighbors(X, return_distance=False)
        array([[1],
               [2]], dtype=int64)
        """
        check_is_fitted(self)
        
        if n_neighbors is None:
            n_neighbors = self.n_neighbors
        else:
            check_n_neighbors(n_neighbors)
                
        if X is not None:
            query_is_train = False
            X = check_array(X)
        else:
            query_is_train = True
            X = self._fit_X
            # Include an extra neighbor to account for the sample 
            # itself being returned, which is removed later.
            n_neighbors += 1
            
        n_samples_fit = self.n_samples_fit_
        if n_neighbors > n_samples_fit:
            raise ValueError('Expected n_neighbors <= n_samples, '
                             f'but n_samples = {n_samples_fit}, '
                             f'n_neighbors = {n_neighbors}.')
            
        d_mat = distance_matrix(X, self._fit_X, self.metric_)
        first_col = 0
        if query_is_train:
            first_col += 1
        neigh_ind = d_mat.argsort(axis=1)[:, first_col : n_neighbors]
        
        if return_distance:
            neigh_dist = np.sort(d_mat, axis=1)[
                :, first_col : n_neighbors]
            return neigh_dist, neigh_ind
        return neigh_ind     
    
    
def check_array(array):
    """
    Checks if input is a 2D array.

    Parameters
    ----------
    array : object
        Input object to check.

    Returns
    -------
    array : ndarray of shape (M, K)
        The validated array.

    Raises
    ------
    ValueError
        If the array is not 2D.
    """
    array = np.asarray(array)
    if array.ndim != 2:
        raise ValueError(
            "Expected 2D array, got {array.ndim}-dimension array "
            f"instead:\narray={array}.\nReshape your data either "
            "using array.reshape(-1, 1) if your data has a "
            "single feature or array.reshape(1, -1) if it contains a "
            "single sample.")
    return array


def check_is_fitted(estimator):
    """
    Checks if the estimator is fitted.
    
    Checks for the presence of fitted attributes (ending with a 
    trailing underscore.)

    Parameters
    ----------
    estimator : object
        Input object to check.

    Returns
    -------
    None

    Raises
    ------
    RuntimeError
        If fitted attributes are not found.
    """
    attributes = [attribute for attribute in vars(estimator) 
                  if attribute.endswith("_")]
    if not attributes:
        raise RuntimeError(
            f"This {type(estimator).__name__} instance is not fitted "
            "yet. Call 'fit' with appropriate arguments before using "
            "this estimator.")
            
            
def check_mnr_mjr_ratio(mnr_mjr_ratio, mnr_cnt, mjr_cnt, method):
    """
    Validates the minority to majority ratio.
    
    Parameters
    ----------
    mnr_mjr_ratio : float
        Desired ratio of majority class observations to minority class
        observations
    mnr_cnt : int
        The number of minority class observations.
    mjr_cnt : int
        The number of majority class observations.
    method : {'oversample', 'undersample'}
        The sampling method being used.

    Returns
    -------
    mnr_mjr_ratio : float
        Desired ratio of majority class observations to minority class
        observations.

    Raises
    ------
    ValueError
        If the minority to majority ratio is invalid.
    """
    msg = ('For your data, the valid interval of '
           'minority to majority ratios is ({:.3f}, {:.3f}). Got '
           '(mnr_mjr_ratio={}).')
    
    if mnr_mjr_ratio <= 0:
        raise ValueError(
            'The minority to majority ratio must be positive. '
            f'Got (mnr_mjr_ratio={mnr_mjr_ratio}).')

    min_ratio = mnr_cnt / mjr_cnt
    max_ratio = inf
    if method == 'oversample':
        if mnr_mjr_ratio < min_ratio:
            raise ValueError(msg.format(min_ratio, max_ratio, 
                                        mnr_mjr_ratio))
    if method == 'undersample':
        max_ratio = mnr_cnt
        if not (min_ratio <= mnr_mjr_ratio <= max_ratio):
            raise ValueError(msg.format(min_ratio, max_ratio, 
                                        mnr_mjr_ratio))
            
    return mnr_mjr_ratio


def check_n_neighbors(n_neighbors):
    """
    Validates number of neighbors.

    Parameters
    ----------
    n_neighbors : object
        Input object to check.

    Returns
    -------
    None

    Raises
    ------
    TypeError or ValueError
        If the number of neighbors is invalid.
    """
    if not isinstance(n_neighbors, Integral):
        raise TypeError('n_neighbors does not take '
                        f'{type(n_neighbors)} value, '
                        'enter integer value.')
    if n_neighbors <= 0:
        raise ValueError('Expected n_neighbors > 0, '
                         f'got {n_neighbors}.')


def class_summary(X, y):
    """
    Summarizes minority and majority class information from data.
    
    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Data matrix.
    y : array-like of shape (n_samples,)
        Corresponding label for each sample in X.
    
    Returns
    -------
    results : dict
        dictionary object, with the following items.
        
        data : ndarray of shape (n_samples, n_features)
            Data matrix.
        target : ndarray of shape (n_samples,)
            Corresponding label for each sample in X.
        labels : tuple of (majority_class_label, minority_class_label)
            Target labels.
        counts : tuple of (majority_class_count, minority_class_count)
            Class counts.
        indices : tuple of (ndarray of shape (majority_class_count,), 
                ndarray of shape (minority_class_count))
            Indices of majority class observations and 
            minority class observations.
    """
    X_c, y_c = np.asarray(X), np.asarray(y)
    class_cnts = pd.Series(y_c).value_counts()
    n_classes = len(class_cnts)
    if n_classes != 2:
        raise ValueError(f'Expected 2 classes, got {n_classes}.')
    major_label, minor_label = class_cnts.index
    major_cnt, minor_cnt = class_cnts
    major_idx = (y_c == major_label).nonzero()[0]
    minor_idx = (y_c == minor_label).nonzero()[0]
    results = {'data': X_c, 'target': y_c,
               'labels': (major_label, minor_label),
               'counts': (major_cnt, minor_cnt),
               'indices': (major_idx, minor_idx)}
    return results


def distance_matrix(x, y, metric='euclidean'):
    """
    Compute the distance matrix.
    
    Returns the matrix of all pairwise distances.
    
    Mimics `scipy.spatial.distance_matrix.`
    
    Parameters
    ----------
    x : array_like of shape (M, K)
        Matrix of M vectors in K dimensions.
    y : array_like of shape (N, K)
        Matrix of N vectors in K dimensions.

    Returns
    -------
    result : ndarray of shape (M, N)
        Matrix containing the distance from every vector in `x` to 
        every vector in `y`.
        
    Examples
    --------
    >>> distance_matrix([[0, 0], [0, 1]], [[1, 0], [1, 1]])
    array([[1.        , 1.41421356],
           [1.41421356, 1.        ]])
    """
    if metric != 'euclidean':
        raise NotImplementedError("distance_matrix only supports "
                                  "metric='euclidean'.")

    x, y = np.asarray(x), np.asarray(y)
    m, k = x.shape
    n, kk = y.shape
    if k != kk:
        raise ValueError(f'x contains {k}-dimensional vectors but '
                         f'y contains {kk}-dimensional vectors.')
        
    result = np.empty((m, n))
    if m < n:
        for i in range(m):
            result[i, :] = euclidean(x[i], y)
    else:
        for j in range(n):
            result[:, j] = euclidean(y[j], x)
    return result


def euclidean(x, y):
    """
    Compute the row-wise Euclidean distance(s) between two arrays.
    
    The Euclidean distance between 1-D arrays `u` and `v`, 
    is defined as
    
    .. math::
    
       {||u-v||}_2 = \\left(\\sum_{i=1}^{n}{(u_i - v_i)^2}\\right)^{1/2}
       
    Mimics `scipy.spatial.distance.euclidean`.
              
    Parameters
    ----------
    x : array_like of shape (M, K) or (K,)
        Input array.
    y : array_like of shape (N, K) or (K,)
        Input array.

    Returns
    -------
    euclidean : ndarray of shape (K,)
        The Euclidean distances between arrays `x` and `y`.
        
    Examples
    --------
    >>> euclidean([1, 0, 0], [0, 1, 0])
    1.4142135623730951
    >>> euclidean([1, 1, 0], [0, 1, 0])
    1.0
    >>> euclidean([0, 0], [[1, 1], [0, 1]])
    array([1.41421356, 1.        ])
    """
    x, y = np.asarray(x), np.asarray(y)
    euclidean = np.sqrt(np.sum((x - y) ** 2, axis=-1))
    return euclidean


def plot_1(profit_mat):
    """
    Plot expected profits per customer for toy classifier with 
    `plot_toy_profit_curve`.
    
    Parameters
    ----------
    profit_mat : array-like of shape (2, 2)
        Profit matrix.
    
    Returns
    -------
    None
    """
    y_labels = [0, 0, 1]
    y_probs = [0.2, 0.6, 0.4]
    
    plot_toy_profit_curve(y_labels, y_probs, profit_mat, 
                          per_instance=True, annotate=True)
    
    # Save plot as 'toy_profit_curve.png'.
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    filename = f'../images/toy_profit_curve_{now}.png'
    plt.savefig(Path(filename), dpi=300)
    print(f'figure saved to {filename}')


def plot_2(profit_mat):
    """
    Plot expected profits per customer with for toy classifier with 
    matplotlib step plot function.
    
    Parameters
    ----------
    profit_mat : array-like of shape (2, 2)
        Profit matrix.
    
    Returns
    -------
    None
    """
    y_labels = [0, 0, 1]
    y_probs = [0.2, 0.6, 0.4]
    exp_profits, thresholds = profit_curve(y_labels, y_probs, 
                                           profit_mat)
    
    pcts = np.linspace(0, 100, len(thresholds))
    fig, ax = plt.subplots(figsize=(8, 4.5), tight_layout=True)
    ax.step(pcts, exp_profits, 'k', where='post', label='Toy Classifier')
    ax.set(title='Profits',
           xlabel='Percentage Of Test Instances (Decreasing By Score)',
           ylabel='Profit')
    ax.legend()
    
    # Save plot as 'toy_profit_curve_v2.png'.
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    filename = f'../images/toy_profit_curve_v2_{now}.png'
    plt.savefig(Path(filename), dpi=300)
    print(f'figure saved to {filename}')
    
    
def plot_3(profit_mat):
    """
    Plot profit curve for logistic regression fit to churn data 
    with `plot_profit_curve`.
    
    Parameters
    ----------
    profit_mat : array-like of shape (2, 2)
        Profit matrix.
    
    Returns
    -------
    None
    """
    X, y = load_churn('../data/churn.csv', return_X_y=True, 
                      as_frame=True)
    # Drop categorical columns.
    X.drop(columns=['State', 'Area Code', 'Phone'], inplace=True)
    # Choosing a random_state makes the split reproducible by others. 
    # 'stratify' forces the test set to have the same class balance as 
    # the original data, which we assume reflects the real-world 
    # class balance. 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=1119, stratify=y)
    
    # `penalty` determines whether the logistic regression is regularized 
    # and how. `max_iter` resolves the warning that the 
    # logistic regression algorithm did not converge.
    lr = LogisticRegression(penalty='none', max_iter=1e4)
    lr.fit(X_train, y_train)
    
    plot_profit_curve(lr, profit_mat, X_test, y_test)    
    
    # Save plot as 'profit_curve_lr.png'.
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    filename = f'../images/profit_curve_lr_{now}.png'
    plt.savefig(Path(filename), dpi=300)
    print(f'figure saved to {filename}')

    
def plot_4(profit_mat):
    """
    Plot profit curve for several models with `plot_profit_curve_v2`.
    
    Parameters
    ----------
    profit_mat : array-like of shape (2, 2)
        Profit matrix.
    
    Returns
    -------
    None
    """
    X, y = load_churn('../data/churn.csv', return_X_y=True, 
                      as_frame=True)
    # Drop categorical columns.
    X.drop(columns=['State', 'Area Code', 'Phone'], inplace=True)
    # Choosing a random_state makes the split reproducible by others. 
    # 'stratify' forces the test set to have the same class balance as 
    # the original data, which we assume reflects the real-world 
    # class balance. 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=1119, stratify=y)
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)

    models = [GBC(), RF(n_jobs=-1), SVC(probability=True), 
              LogisticRegression(penalty='none')]
    random_state = 1310
    for i, model in enumerate(models):
        model.set_params(**{'random_state': random_state})
        model.fit(X_train_std, y_train)

    fig, ax = plt.subplots(figsize=(16, 9), tight_layout=True)
    for model in models:
        plot_profit_curve_v2(model, profit_mat, X_test_std, y_test, ax=ax)
        
    # Add profit matrix.
    tp_profit, fp_profit, fn_profit, tn_profit = profit_mat.ravel()
    table = [['Profit', 'Actual +', 'Actual -'], 
             ['Predicted +', tp_profit, fp_profit],
             ['Predicted -', fn_profit, tn_profit]]
    ax.table(cellText=table, cellLoc='center', colWidths=[0.1] * 3, 
             loc='lower left')
    
    # Save plot as 'profit_curve_4models.png'.
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    filename = f'../images/profit_curve_4models_{now}.png'
    plt.savefig(Path(filename), dpi=300)
    print(f'figure saved to {filename}')
    
    
def plot_5(clf, random_state=1):
    """Plot the effect of different sampling methods on a 
    classifier's decision boundary.
    
    Parameters
    ----------
    clf : estimator instance
        Classifier or a pipeline in which the 
        last estimator is a classifier.
        
    random_state : int or None, default=None
        Determines random number generation for dataset creation. Pass 
        an int for reproducible output across multiple function calls.
        
    Returns
    -------
    None
    """
    X, y = make_classification(
        n_samples=10000, n_features=2, n_redundant=0, 
        n_clusters_per_class=1, weights=[0.99], flip_y=0, 
        random_state=random_state)
    titles = ['Original Data', 'Undersample', 'Oversample', 'SMOTE']
    samplers = [None, 
                Undersample(random_state=random_state), 
                Oversample(random_state=random_state),
                SMOTE_v2(random_state=random_state)]

    # Step size in the mesh.
    h = 0.02
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['red', 'blue'])

    fig, axs = plt.subplots(2, 2, figsize=(8.5, 8), tight_layout=True)
    for i, (title, sampler, ax) in enumerate(zip(titles, samplers, 
                                                 axs.flat)):
        X_s, y_s = X, y
        if sampler:
            X_s, y_s = sampler.fit_resample(X, y)
        y_cnt = Counter(y_s)
        clf.fit(X_s, y_s)
        
        # Plot the decision boundary. For that, we will assign a color to 
        # each point in the mesh [x_min, x_max]x[y_min, y_max].
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)
        # Plot the training points
        ax.scatter(X_s[:, 0], X_s[:, 1], c=y_s, alpha=0.6, cmap=cm_bright,
                   edgecolors='k')
        ax.axis('scaled')
        ax.set(title=f'{title}, y={{0: {y_cnt[0]}, 1: {y_cnt[1]}}}',
               xlim=(xx.min(), xx.max()), xticks=(),
               ylim=(yy.min(), yy.max()), yticks=())
    if clf.__class__.__name__ == 'Pipeline':
        suptitle = clf['clf'].__class__.__name__
    else:
        suptitle = clf.__class__.__name__
    fig.suptitle(suptitle, size='xx-large')
    
    # Save plot as 'sampling_methods.png'.
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    filename = f'../images/sampling_methods_{now}.png'
    plt.savefig(Path(filename), dpi=300)
    print(f'figure saved to {filename}')


def do_sampling_study(churnpath, profit_mat, *, n_props=5, mnr_props=None):
    """Study the effect of different sampling methods on 
    expected profit using the churn dataset.
    
    Parameters
    ----------
    churnpath : str
        File path for churn.csv.
    profit_mat : array-like of shape (2, 2)
        Profit matrix with payoffs corresponding to:
            -----------
            | TP | FP |
            -----------
            | FN | TN |
            -----------        
    n_props : int, default=5
        Number of minority proportions to investigate. 
        Minority proportions will be generated as an evenly spaced 
        sequence in the interval [starting minority proportion, 
            starting minority count / (starting minority count + 1)].
    mnr_props : array-like of shape (n_props,), default=None
        An array of minority class proportions to investigate. Will 
        override n_props if provided.
            
    Returns
    -------
    df_data : pandas DataFrame
        DataFrame containing sampling study results.        
    """
    start = datetime.now()
    random_states = [129, 140, 2350]
    samp_labels = ['Undersample', 'Oversample', 'SMOTE']
    samp_methods = [Undersample, Oversample, SMOTE_v2]
    # Create an sklearn pipeline instance that standardizes features 
    # before fitting a model. SMOTE relies on nearest neighbors, which is 
    # influenced by feature sizes.
    pipe = Pipeline([
        ('scaler', StandardScaler()), 
        ('clf', LogisticRegression(penalty='none', max_iter=1e4))])
    X, y = load_churn(churnpath, return_X_y=True, as_frame=True)
    # Drop categorical columns.
    X.drop(columns=['State', 'Area Code', 'Phone'], inplace=True)
    
    if mnr_props is None:
        n_iter = len(random_states) * len(samp_methods) * n_props
    else:
        n_iter = len(random_states) * len(samp_methods) * len(mnr_props)
    time_iter = 3.5691
    est_sec = n_iter * time_iter
    est_min = int(est_sec // 60)
    rem_sec = round(est_sec - (60 * est_min))
    print(f'Estimated time: {est_min:>2} min {rem_sec:>2} s')
    
    data = []
    iteration = 1
    for random_state in random_states:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, random_state=random_state, stratify=y)
        if mnr_props is None:
            # Calculate minimum and maximum possible 
            # minority to majority class ratios.
            mjr_cnt, mnr_cnt = np.bincount(y_train)
            min_ratio = mnr_cnt / mjr_cnt
            max_ratio =  mnr_cnt / (mnr_cnt + 1)
            # Calculate minority proportions up to 2 decimals.
            mnr_props = np.linspace(min_ratio, max_ratio, n_props, 
                                    endpoint=False)
        mnr_mjr_ratios = mnr_props / (1 - mnr_props)

        for mnr_prop, mnr_mjr_ratio in zip(mnr_props, mnr_mjr_ratios):
            for samp_label, samp_method in zip(samp_labels, 
                                               samp_methods):
                sampler = samp_method(mnr_mjr_ratio=mnr_mjr_ratio, 
                                      random_state=random_state)
                X_samp, y_samp = sampler.fit_resample(X_train, y_train)
                pipe.fit(X_samp, y_samp)

                y_probs = pipe.predict_proba(X_test)[:, 1]
                exp_profits, thresholds = profit_curve(y_test, y_probs, 
                                                       profit_mat)
                df = pd.DataFrame({'exp_profit': exp_profits, 
                                   'threshold': thresholds})

                df['random_state'] = random_state
                df['samp_method'] = samp_label
                df['mnr_mjr_ratio'] = mnr_mjr_ratio
                df['mnr_prop'] = mnr_prop
                df['ml_algo'] = pipe['clf'].__class__.__name__

                def arr_less_than_thold(row):
                    """Helper function to compare whether current 
                    threshold is less than the other thresholds.
                    """
                    mask_same_name = df['ml_algo'] == row['ml_algo']
                    less_than_threshold = (
                        row['threshold'] < df[mask_same_name]['threshold'])
                    return less_than_threshold

                less_than_thold = df.apply(arr_less_than_thold, axis=1)
                df['top_n_prop'] = less_than_thold.mean(axis=1)
                df['n_targeted'] = less_than_thold.sum(axis=1)
                df['n_customers'] = len(y_samp)
                data.append(df)
                
                elapsed_sec = (datetime.now() - start).seconds
                elapsed_min = elapsed_sec // 60
                remainder_sec = elapsed_sec - (elapsed_min * 60)
                print(f'Completed: {iteration:>3} of {n_iter}. Time elapsed: '
                      f'{elapsed_min:>2} min {remainder_sec:>2} s', 
                      end='\r')
                iteration += 1
    
    print(f'Completion time: {elapsed_min:>2} min {remainder_sec:>2} s')
    df_data = pd.concat(data)
    # Save data as 'sampling_study.csv'.
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    filename = Path(f'../data/sampling_study_{now}.csv')
    df_data.to_csv(filename, index=False)
    print(f'data saved to {filename}')
    
    return df_data

    
if __name__ == "__main__":
    # Creates the plots in the assignment.
    plt.style.use('ggplot')
    profit_mat = np.array([[3, -1], [0, 0]])
    plot_1(profit_mat)
    plot_2(profit_mat)    
    plot_3(profit_mat)    
    plot_4(profit_mat)
    plot_5(LogisticRegression(penalty='none'))
    mnr_props = np.linspace(0.17, 0.98, int(82/2)).round(2)
    do_sampling_study('../data/churn.csv', profit_mat, mnr_props=mnr_props)