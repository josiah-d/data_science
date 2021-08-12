import numpy as np
from pymongo import MongoClient
from nltk.tokenize import word_tokenize, wordpunct_tokenize, RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB as SKMultinomialNB
from naive_bayes import MultinomialNaiveBayes


def load_data():
    client = MongoClient()
    db = client.nyt_dump
    coll = db.articles

    articles = coll.find({'$or': [{'section_name': 'Sports'},
                                  {'section_name': 'Fashion & Style'}]})

    article_texts = []
    labels = []
    for article in articles:
        article_texts.append(' '.join(article['content'])),
        labels.append(article['section_name'])
    return article_texts, np.array(labels)


def my_tokenizer(doc):
    tokenizer = RegexpTokenizer(r'\w+')
    article_tokens = tokenizer.tokenize(doc.lower())
    return article_tokens


if __name__ == '__main__':
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    X_tr_toks = [my_tokenizer(doc) for doc in X_train]
    X_te_toks = [my_tokenizer(doc) for doc in X_test]

    cv = CountVectorizer(tokenizer=my_tokenizer)
    X_tr_vec = cv.fit_transform(X_train)
    X_te_vec = cv.transform(X_test)

    print()

    print("My Implementation:")
    my_nb = MultinomialNaiveBayes()
    my_nb.fit(X_tr_toks, y_train)
    print('Test Accuracy:', my_nb.score(X_te_toks, y_test))
    my_predictions = my_nb.predict(X_te_toks)

    print('\nWords with the highest Sports odds')
    sports_odds = []
    for word in my_nb.vocab:
        p_sports = my_nb._word_likelihood(word, 'Sports')
        p_fashion = my_nb._word_likelihood(word, 'Fashion & Style')
        sports_odds.append(p_sports / p_fashion)
    print(my_nb.vocab[np.argsort(sports_odds)[-11:]])

    print('\nWords with the highest Fashion odds')
    print(my_nb.vocab[np.argsort(sports_odds)[:10]])

    print("\nsklearn's Implementation")
    mnb = SKMultinomialNB()
    mnb.fit(X_tr_vec, y_train)
    print('Test Accuracy:', mnb.score(X_te_vec, y_test))
    sklearn_predictions = mnb.predict(X_te_vec)

    # Assert I get the same results as sklearn
    # (will give an error if different)
    assert np.all(sklearn_predictions == my_predictions)
