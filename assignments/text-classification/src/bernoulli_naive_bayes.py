from collections import Counter, defaultdict
import numpy as np
import itertools

class BernoulliNaiveBayes(object):
    """
    Attributes
    ----------
    alpha : float
        Laplace smoothing constant.

    Methods
    -------
    fit(X, y)
        Create the lookup dictionaries used to calculate likelihoods
    predict(X)
        Hard-classify data with the fitted Naive Bayes model
    """
    def __init__(self, alpha=1.0):
        """
        Parameters
        ----------
        alpha : float
            Laplace smoothing constant.  Default is 1, which means something
            that had never been seen before would be assigned a probability of
            1/2 of appearing in a document
        """
        # number of documents of each class
        self.class_counts = defaultdict(int)

        # number of documents for each word for each class
        self.class_feature_counts = defaultdict(Counter)

        self.alpha = float(alpha)
        
        # number of features (number of unique words)
        self.p = None
        self.vocab = set()

    def _compute_likelihoods(self, X, y):
        '''Populates class_counts and class_feature_counts

        Parameters
        ----------
        X : Two-dimensional array-like
            Array of input features, with each inner object representing a
            document or observation
        y : Numpy array
            Array of class labels (e.g. spam / not spam)
        '''
        pass

    def fit(self, X, y):
        '''Fits a Naive Bayes model to explain the relationship between X and y

        Parameters
        ----------
        X : Two-dimensional array-like
            Array of input features, with each inner object representing a
            document or observation
        y : Numpy array
            Array of class labels (e.g. spam / not spam)
        '''

        # Compute number of features, aka the number of unique words (vocabulary)
        for document in X:
            for word in document:
                self.vocab.add(word)
        self.p = len(self.vocab)

        # Compute document count for each word for each class
        self._compute_likelihoods(X, y)

    def posteriors(self, X):
        '''Calculates the log-likelihood of each class for each input data point

        Parameters
        ----------
        X : Two-dimensional array-like
            Array of input features, with each inner object representing a
            document or observation

        Returns
        -------
        posteriors : list of dictionaries
            Each dictionary represents the predicted probability of being in a
            particular class, where key=label and value=prediction

        Notes
        -----
        The Naive Bayes class allows targets besides just zero and one, and a
        list of dictionaries enables this functionality
        '''

        #Make sure you implement Laplace smoothing when calculating probabilities!

        #This is what your output should look like - a list of dictionaries
        sample = [{"some_class":.123, "some_other_class":.451},
                  {"some_class":.888, "some_other_class":.177}]

        return sample 

    def predict(self, X):
        """Uses a fitted Naive Bayes model to predict class labels

        Parameters
        ----------
        X : Two-dimensional array-like
            Array of input features, with each inner object representing a
            document or observation

        Returns
        -------
        predictions : Numpy array
            Vector of class predictions for provided data X
        """
        predictions = []

        #Iterate through each dictionary
        for post in self.posteriors(X):
            #Find the label that corresponds to the highest probability
            pred = max(post.keys(), key=(lambda label: post[label]))
            predictions.append(pred)
        return np.array(predictions)

    def score(self, X, y):
        """Calculates the accuracy, the percentage of correct predictions

        Parameters
        ----------
        X : Two-dimensional array-like
            Array of input features, with each inner object representing a
            document or observation

        Returns
        -------
        accuracy : float
            A number representing the classification accuracy on data X
        """

        return np.mean(self.predict(X) == y)
