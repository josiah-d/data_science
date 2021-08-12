import re

import numpy as np
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.externals import joblib
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, CountVectorizer
from sklearn.metrics.pairwise import cosine_distances, euclidean_distances
from sklearn.model_selection import GridSearchCV, train_test_split

pd.options.display.max_columns = 30

stop_words = ENGLISH_STOP_WORDS.union({'film', 'directed', 'fictional', 'work', 'books', 'released', 'written', 'born', 'characters', 'television', 'episodes', 'director', 'novel', 'story', 'book', 'list',
                                       'element', 'redirect', 'starring', 'fiction', 'story', 'produced', 'novel', 'based', 'character', 'game', 'comic', 'television', 'animated', 'tv', 'series', 'redirects', 'mentions', 'locations'})

class TopicModeler(object):
    """
    Topic Modeler
    ---------
    model : type of sklearn model to use (currently set up for LDA  but could be extended to NMF and others)
    vectorizer : sklearn vectorizer (currently set up for CountVectorizer but could be extended to use TfIDF)
    distance_func : sklearn.pairwise function for determining distance between documents
    """

    def __init__(self, model, vectorizer, distance_func=cosine_distances):
        self.model = model
        self.text = None
        self.titles = None
        self.vectorizer = vectorizer
        self.feature_names = None
        self.doc_probs = None
        self.distance_func = distance_func
        self.word_vec = None

    def set_feature_names(self):
        """
        Sets feature names from vectorizer
        Args:
            None

        Returns:
            None
        """
        self.feature_names = np.array(self.vectorizer.get_feature_names())

    def vectorize(self):
        """
        Vectorizes corpus

        Args:
            None

        Returns:
            type: np.array of vectorized text

        """

        print('Vectorizing...')
        return self.vectorizer.fit_transform(self.text)

    def fit(self, text, titles=None):
        """
        Vectorizes corpus and fits model with it. Titles can be set here as well

        Args:
            text (iterable of strings): Array for documents
            titles (pd.Series(str) or np.array(str)): Article titles

        Returns:
            None
        """

        self.text = text
        self.word_vec = self.vectorize()
        print('Fitting...')
        self.model.fit(self.word_vec)
        self.set_feature_names()
        self.titles = titles

    def top_topic_features(self, num_features=10):
        """
        Takes the n most important features for each topic and indexes against the vectorizer to return the labels associated with those features.

        Args:
            num_features (int): number of features to return

        Returns:
            top_feature names (np.array(str)): top feature labels
            """

        # Argsort along rows, reverse the order of the rows, then take all rows up to the number of features
        sorted_topics = self.model.components_.argsort(axis=1)[:, ::-1][:, :num_features]

        # Index the feature names based on the indices of the top most important features
        return self.feature_names[sorted_topics]

    def predict_proba(self, text):
        """
        Vectorizes and transforms text to give the topic probabilities for each document

        Args:
            text (iterable of strings): Array for documents

        Returns:
            np.array(float64): document by topic probabilities
            """

        # Convert single document to iterable
        if type(text) == str:
            text = [text]

        vec_text = self.vectorizer.transform(text)
        return self.model.transform(vec_text)

    def sort_by_distance(self, doc_index, doc_probs):
        """
        Finds indices of closest (most similar) articles based on document by probability array
        Args:
            doc_index (int): row index of selected document
            doc probs (np.array(float64)): document by topic probabilities

        Returns:
            np.array(int): array containing sorted indices of most similar documents
            """

        distances = self.distance_func(doc_probs[doc_index, np.newaxis], doc_probs)
        return distances.argsort()

    def find_closest_document_titles(self, sorted_indices, num_documents=10):
        """
        Returns the document titles of most similar documents

        Args:
            sorted_indices (np.array(int)): array with sorted document indices, where the target document is index [0]

        Returns:
            dicionary: key = target document title, value = list of similar document titles
            """

        name_array = self.titles.iloc[sorted_indices.ravel()][:num_documents]
        return {name_array.iloc[0]: name_array.iloc[1:].tolist()}

    def find_article_idx(self, article_title):
        """
        Returns article title
        Args:
            article_title (str): target article title

        Returns:
            int: index of article
            """
        return self.titles[self.titles == article_title].index[0]

    def top_closest_articles(self, article_title, num_documents=10):
        """
        Returns most similar articles given article title
        Args:
            article_title (str): target article title
            num_documents (int): number of similar documents to return

        Returns:
            dicionary: key = target document title, value = list of similar document titles
            """

        doc_index = self.find_article_idx(article_title)
        doc_probs = self.predict_proba(self.text)
        article_similarities = self.sort_by_distance(doc_index, doc_probs)
        return self.find_closest_document_titles(article_similarities, num_documents)

    def grid_search_lda(self, params):
        """
        Performs grid search optimizing log-loss using topic model

        Args:
            params (dict): dictionary of grid search arguments, key = sklearn model keyword argument, value = values to try

        Returns:
            sklearn GridSearchCV object of best cross validated model
            """

        # Create holdout set to check log loss on unseen data
        X_train, X_test = train_test_split(self.word_vec, test_size=0.25)
        lda_cv = GridSearchCV(self.model, param_grid=params, n_jobs=-1,  verbose=1)
        lda_cv.fit(X_train)

        print(pd.DataFrame.from_dict(lda_cv.cv_results_))
        print('Test Score:', lda_cv.score(X_test))
        return lda_cv

    def load_model(self, filepath):
        """
        Load topic model object

        Args:
            filepath (str): filepath to load from

        Returns:
            None
            """
        self.model = joblib.load(filepath)

    def load_vectorizer(self, filepath):
        """
        Load vectorizer object

        Args:
            filepath (str): filepath to load from

        Returns:
            None
            """
        self.tf_vectorizer = joblib.load(filepath)

    def save_model(self, filepath):
        """
        Save topic model object

        Args:
            filepath (str): filepath to save to

        Returns:
            None
            """
        joblib.dump(self.model, filepath)

    def save_vectorizer(self, filepath):
        """
        Save vectorizer object

        Args:
            filepath (str): filepath to save to

        Returns:
            None
            """
        joblib.dump(self.vectorizer, filepath)


def load_data():
    """
    Loads data from wikipedia CSV

    Args:
        None
    Returns:
        pd.DataFrame: Text, titles and pageid from a download of paranormal related wikipedia articles
        """
    df = pd.read_csv('data/spooky_wikipedia.csv', index_col=0)
    list_articles = df.title.str.lower().str.contains('list of')
    df = df[~list_articles]
    df = df.dropna()
    return df


def main():
    df = load_data() #add this make a sample .sample(100).reset_index(drop=True)
    lda = LatentDirichletAllocation(n_components=30, learning_offset=50., verbose=1,
                                    doc_topic_prior=0.9, topic_word_prior=0.9, n_jobs=-1, learning_method='online')
    tf_vectorizer = CountVectorizer(max_df=0.85, min_df=2, max_features=1000, stop_words=stop_words)
    tm = TopicModeler(lda, tf_vectorizer)
    tm.fit(df.text, titles=df.title)

    print(tm.top_topic_features())

    print(tm.top_closest_articles(df.title.iloc[5]))
    print(tm.top_closest_articles('Alchemy'))
    print(tm.top_closest_articles('Chupacabra'))
    print(tm.top_closest_articles('Ghost'))

    # Commented out because this can take a really long time!
    # params = {"n_components": [2, 5, 10, 50, 75, 100, 200]}
    # grid_search = tm.grid_search_lda(params)
    # joblib.dump(grid_search, 'grid_search.joblib')
    # A grid search across many values yielded these values for optimizing log loss:
    # {'doc_topic_prior': 0.25, 'n_components': 5, 'topic_word_prior': 0.5}


if __name__ == '__main__':
    main()
