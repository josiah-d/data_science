'''
This script provides functions to read & analyze the contents of NYT articles
using our custom NMF class -and- using the NMF implementation from scikit-learn.

For a discussion of this script, see `pair.ipynb`.
'''

import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF as NMF_sklearn

from my_nmf import NMF


def build_text_vectorizer(contents, use_tfidf=True, use_stemmer=False, max_features=None):
    '''
    Build and return a **callable** for transforming text documents to vectors,
    as well as a vocabulary to map document-vector indices to words from the
    corpus. The vectorizer will be trained from the text documents in the
    `contents` argument. If `use_tfidf` is True, then the vectorizer will use
    the Tf-Idf algorithm, otherwise a Bag-of-Words vectorizer will be used.
    The text will be tokenized by words, and each word will be stemmed iff
    `use_stemmer` is True. If `max_features` is not None, then the vocabulary
    will be limited to the `max_features` most common words in the corpus.
    '''
    Vectorizer = TfidfVectorizer if use_tfidf else CountVectorizer
    tokenizer = RegexpTokenizer(r"[\w']+")
    stem = PorterStemmer().stem if use_stemmer else (lambda x: x)
    stop_set = set(stopwords.words('english'))

    # Closure over the tokenizer et al.
    def tokenize(text):
        tokens = tokenizer.tokenize(text)
        stems = [stem(token) for token in tokens if token not in stop_set]
        return stems

    vectorizer_model = Vectorizer(tokenizer=tokenize, max_features=max_features)
    vectorizer_model.fit(contents)
    vocabulary = np.array(vectorizer_model.get_feature_names())

    # Closure over the vectorizer_model's transform method.
    def vectorizer(X):
        return vectorizer_model.transform(X).toarray()

    return vectorizer, vocabulary


def softmax(v, temperature=1.0):
    '''
    A heuristic to convert arbitrary positive values into probabilities.
    See: https://en.wikipedia.org/wiki/Softmax_function
    '''
    expv = np.exp(v / temperature)
    s = np.sum(expv)
    return expv / s


def hand_label_topics(H, vocabulary):
    '''
    Print the most influential words of each latent topic, and prompt the user
    to label each topic. The user should use their humanness to figure out what
    each latent topic is capturing.
    '''
    hand_labels = []
    for i, row in enumerate(H):
        top_five = np.argsort(row)[::-1][:20]
        print('topic', i)
        print('-->', ' '.join(vocabulary[top_five]))
        label = input('please label this topic: ')
        hand_labels.append(label)
        print()
    return hand_labels


def analyze_article(article_index, contents, web_urls, W, hand_labels):
    '''
    Print an analysis of a single NYT articles, including the article text
    and a summary of which topics it represents. The topics are identified
    via the hand-labels which were assigned by the user.
    '''
    print(web_urls[article_index])
    print(contents[article_index])
    probs = softmax(W[article_index], temperature=0.01)
    for prob, label in zip(probs, hand_labels):
        print('--> {:.2f}% {}'.format(prob * 100, label))
    print()


def main():
    '''
    Run the unsupervised analysis of the NYT corpus, using NMF to find latent
    topics. The user will be prompted to label each latent topic, then a few
    articles will be analyzed to see which topics they contain.
    '''
    # Load the corpus.
    df = pd.read_pickle("data/articles.pkl")
    contents = df.content
    web_urls = df.web_url

    # Build our text-to-vector vectorizer, then vectorize our corpus.
    vectorizer, vocabulary = build_text_vectorizer(contents,
                                 use_tfidf=True,
                                 use_stemmer=False,
                                 max_features=5000)
    X = vectorizer(contents)

    # We'd like to see consistent results, so set the seed.
    np.random.seed(12345)

    # Find latent topics using our NMF model.
    factorizer = NMF(k=7, max_iters=35, alpha=0.5)
    W, H = factorizer.fit(X, verbose=True)

    # Label topics and analyze a few NYT articles.
    # Btw, if you haven't modified anything, the seven topics which should
    # pop out are:  (you should type these as the labels when prompted)
    #  1. "football",
    #  2. "arts",
    #  3. "baseball",
    #  4. "world news (middle eastern?)",
    #  5. "politics",
    #  6. "world news (war?)",
    #  7. "economics"
    hand_labels = hand_label_topics(H, vocabulary)
    rand_articles = np.random.choice(list(range(len(W))), 15)
    for i in rand_articles:
        analyze_article(i, contents, web_urls, W, hand_labels)

    # Do it all again, this time using scikit-learn.
    nmf = NMF_sklearn(n_components=7, max_iter=100, random_state=12345, alpha=0.0)
    W = nmf.fit_transform(X)
    H = nmf.components_
    print('reconstruction error:', nmf.reconstruction_err_)
    hand_labels = hand_label_topics(H, vocabulary)
    for i in rand_articles:
        analyze_article(i, contents, web_urls, W, hand_labels)


if __name__ == '__main__':

    main()
