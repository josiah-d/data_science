from pymongo import MongoClient, errors
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

client = MongoClient()
coll = client.nyt_dump.articles

# Tokenize and stop words

# 1. Create a set of documents.
documents = [' '.join(article['content']).lower() for article in coll.find()]

# 2. Create a set of tokenized documents.
docs = [word_tokenize(content) for content in documents]

# 3. Strip out stop words from each tokenized document.
stop = set(stopwords.words('english'))
docs = [[word for word in words if word not in stop] for words in docs]


# Stemming / Lemmatization

# 1. Stem using both stemmers and the lemmatizer
porter = PorterStemmer()
snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()
docs_porter = [[porter.stem(word) for word in words] for words in docs]
docs_snowball = [[snowball.stem(word) for word in words] for words in docs]
docs_wordnet = [[wordnet.lemmatize(word) for word in words] for words in docs]

# Compare
for i in range(min(len(docs_porter[0]), len(docs_snowball[0]), len(docs_wordnet[0]))):
    p, s, w = docs_porter[0][i], docs_snowball[0][i], docs_wordnet[0][i]
    if len(set((p, s, w))) != 1:
        print("{}\t{}\t{}\t{}".format(docs[0][i], p, s, w))


# Part of speech tagging

# 1. Create a part of speech tagged version of your already tokenized dataset.
# commented out because it is slow...
#pos_tagged = [pos_tag(tokens) for tokens in docs]


# Bag of words and TF-IDF

# 1. Create vocab, set of unique words
docs = docs_snowball # choose which stemmer/lemmatizer to use
vocab_set = set()
[[vocab_set.add(token) for token in tokens] for tokens in docs]
vocab = list(vocab_set)

# 2. Create word count vectors manually.
matrix = [[0] * len(vocab) for doc in docs]
vocab_dict = dict((word, i) for i, word in enumerate(vocab))
for i, words in enumerate(docs):
    for word in words:
        matrix[i][vocab_dict[word]] += 1

# 3. Create word count vector over the whole corpus.
cv = CountVectorizer(stop_words='english')
vectorized = cv.fit_transform(documents)

tfidf = TfidfVectorizer(stop_words='english')
tfidfed = tfidf.fit_transform(documents)


# Cosine Similarity using TF-IDF

# 1. Compute cosine similarity
cosine_similarities = linear_kernel(tfidfed, tfidfed)

# 2. Print out similarities
for i, doc1 in enumerate(docs):
    for j, doc2 in enumerate(docs):
        print(i, j, cosine_similarities[i, j])
