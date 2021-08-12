from collections import Counter, defaultdict
import numpy as np
import itertools

class MultinomialNaiveBayes(object):
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
            1 / the number of features
        """
        # number of documents per class
        self.class_counts = defaultdict(int)

        # count of each word for each class
        self.class_feature_counts = defaultdict(Counter)

        # total word count for each class
        self.class_total_feature_counts = defaultdict(int)

        self.alpha = float(alpha)

        # number of features (number of unique words)
        # (used in laplacian smoothing)
        self.p = None

    def _compute_likelihoods(self, X, y):
        '''Populates class_counts, class_feature_counts, and class_total_feature_counts

        Parameters
        ----------
        X : Two-dimensional array-like
            Array of input features, with each inner object representing a
            document or observation
        y : Numpy array
            Array of class labels (e.g. spam / not spam)
        '''

        for doc, label in zip(X, y):
            self.class_counts[label] += 1
            self.class_total_feature_counts[label] += len(doc)
            self.class_feature_counts[label].update(Counter(doc))            

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

        # Compute number of features, aka the number of unique words
        unique_words = set()
        for document in X:
            for word in document:
                unique_words.add(word)
        self.vocab = np.array(list(unique_words))
        self.p = len(unique_words)

        # Compute word count for each word for each class
        # as well as total word count for each class
        self._compute_likelihoods(X, y)

    def _word_likelihood(self, word, label):
        numerator = (self.alpha  + self.class_feature_counts[label][word])
        denominator = (self.alpha*self.p + self.class_total_feature_counts[label])
        return numerator / denominator

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
            Each dictionary represents the predicted likelihood of being in a
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
        total_docs = sum(self.class_counts.values())
        posts = []
        for doc in X:
            post = {}
            for label in self.class_total_feature_counts:
                log_prob = np.log(self.class_counts[label]/total_docs)
                for word in doc:
                    like = self._word_likelihood(word, label)
                    log_prob += np.log(like)
                post[label] = log_prob
            posts.append(post)
        return posts


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
