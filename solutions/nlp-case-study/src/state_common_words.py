# Import Modules
from collections import Counter
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import json
from pprint import pprint
import string
from sklearn.feature_extraction.text import TfidfVectorizer

# NLTK Modules
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from src.cleaner import clean_data
from src.helpers import *

def common_words(df):
    clean_df = df.copy()

    # Create Documents
    documents = clean_df['content']

    # Set Stop Words
    stop = set(stopwords.words('english'))
    # Set Stop Punctuations
    puncs = set(string.punctuation)
    # Merge Stops
    full_stop = stop.union(puncs)
    # full_stop

    # Tokenize Words from Documents
    tokens = [word_tokenize(doc.lower()) for doc in documents]

    # Filter each token for stop words
    doc_filter = [filter_tokens(token, full_stop) for token in tokens]

    snowball = SnowballStemmer('english')

    docs_snowball = [[snowball.stem(word) for word in words]
                 for words in doc_filter]

    # Stem Words in Each Document
    clean_tokens = [list(map(snowball.stem, sent)) for sent in doc_filter]
    # clean_tokens

    # Check for stray tokens (ones with weird puncs, not alphabetical strings)
    strays = []
    for i in range(len(clean_tokens)):
    #     print("--- sentence tokens (lemmatize): {}".format(tokens_lemmatize[i]))
        for word in clean_tokens[i]:
            if not word.isalpha():
                strays.append(word)
    set(strays)

    # Documents to series
    document_series = pd.Series([" ".join(x) for x in clean_tokens])

    # term occurence = counting distinct words in each bag
    term_occ = [Counter(doc) for doc in clean_tokens]
    # term_occ
    term_freq = list()
    for i in range(len(clean_tokens)):
        term_freq.append( {k: (v / float(len(clean_tokens[i])))
                        for k, v in term_occ[i].items()} )

    # Get Document Frequencies
    doc_occ = Counter( [word for token in clean_tokens for word in set(token)] )

    doc_freq = {k: (v / float(len(clean_tokens)))
                for k, v in doc_occ.items()}

    # doc_freq

    # See words with a high frequency threshhold 50%
    thresh = 0.5
    for word, freq in doc_freq.items():
        if freq >= thresh:
            pass
            #print(f"{word}:  {freq}")

    # Get Vocabulary

    # the minimum document frequency (in proportion of the length of the corpus)
    min_df = 0.5

    # filtering items to obtain the vocabulary
    vocabulary = [ k for k,v in doc_freq.items() if v >= min_df ]

    # print vocabulary
    #print ("-- vocabulary (len={}): {}".format(len(vocabulary),vocabulary))

    x = np.arange(0.1, 1.1, 0.1)

    all_vocabs = [[ k for k,v in doc_freq.items() if v >= thresh ] for thresh in x]
    for vocab in all_vocabs:
        pass
        #pprint("-- vocabulary (len={}): {}".format(len(vocab),vocab))

    return all_vocabs
