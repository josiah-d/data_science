Loading your data from Mongo
===========================================

1. After doing the above import, load all of the article content from the collection into a list of strings where each individual string is a NY Times article. Note that the `"content"` field is a list of strings. You should just join these together, separated by white space.

    ```python
    from pymongo import MongoClient

    client = MongoClient()
    db = client.nyt_dump
    coll = db.articles
    documents = ['\n'.join(article['content']) for article in coll.find()]
    ```

Tokenization and Stop words
====================================

1. Use nltk's [word_tokenize](http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.punkt.PunktLanguageVars.word_tokenize) to tokenize the documents.

    ```python
    from nltk.tokenize import word_tokenize

    tokenized = [word_tokenize(content.lower()) for content in documents]
    ```

2. Remove all the stop words. You should use nltk's stopwords (check out section 4.1 in [nltk book ch 2](http://www.nltk.org/book/ch02.html)).

    ```python
    from nltk.corpus import stopwords

    stop = set(stopwords.words('english'))
    docs = [[word for word in words if word not in stop]
            for words in tokenized]
    ```

Stemming/Lemmatization
====================================================

1. Try running both stemmers and the lemmatizer on the documents. They only modify one word at a time, so you'll need to do a double for loop to apply the stemmer/lemmatizer to each word in all the documents.

    ```python
    from nltk.stem.porter import PorterStemmer
    from nltk.stem.snowball import SnowballStemmer
    from nltk.stem.wordnet import WordNetLemmatizer

    porter = PorterStemmer()
    snowball = SnowballStemmer('english')
    wordnet = WordNetLemmatizer()

    docs_porter = [[porter.stem(word) for word in words]
                   for words in docs]
    docs_snowball = [[snowball.stem(word) for word in words]
                     for words in docs]
    docs_wordnet = [[wordnet.lemmatize(word) for word in words]
                    for words in docs]
    ```

2. Compare the results. What do you notice are the differences between the two stemmers and the lemmatizer? Write your results as comments in your code!

    ```python
    ## Print the stemmed and lemmatized words from the first document
    print("%16s %16s %16s %16s" % ("word", "porter", "snowball", "lemmatizer"))
    for i in range(min(len(docs_porter[0]), len(docs_snowball[0]), len(docs_wordnet[0]))):
        p, s, w = docs_porter[0][i], docs_snowball[0][i], docs_wordnet[0][i]
        if len(set((p, s, w))) != 1:
            print("%16s %16s %16s %16s" % (docs[0][i], p, s, w))
    ```

    Results (some of the ones that are different):
    ```
            word           porter         snowball       lemmatizer
         abetted             abet             abet          abetted
          grated            grate            grate           grated
          cooked             cook             cook           cooked
       underdone         underdon         underdon        underdone
         crisped            crisp            crisp          crisped
    ```

3. Choose one of the 3 to use from here on out.

    ```python
    my_docs = docs_snowball
    ```

Bag Of Words and TFIDF
===================================================

1. Create your vocab, a set of words UNIQUE over the whole corpus (list of documents which are lists of strings). A `set` is a good datatype for this since it doesn't allow duplicates. At the end you'll want to convert it to a list so that we can deal with our words in a consistent order.

    ```python
    vocab_set = set()
    [[vocab_set.add(token) for token in tokens] for tokens in my_docs]
    vocab = list(vocab_set)
    ```

2. Create a reverse lookup for the vocab list. This is a dictionary whose keys are the words and values are the indices of the words (the word id). This will make things much faster than using the list `index` function.

    ```python
    vocab_dict = {word: i for i, word in enumerate(vocab)}
    ```

3. Now let's create our word count vectors manually. Create a numpy matrix where each row corresponds to a document and each column a word. The value should be the count of the number of times that word appeared in that document.

    ```python
    import numpy as np

    word_counts = np.zeros((len(docs), len(vocab)))
    for doc_id, words in enumerate(my_docs):
        for word in words:
            word_id = vocab_dict[word]
            word_counts[doc_id][word_id] += 1
    ```

4. Create the document frequencies. For each word, get a count of the number of documents the word appears in (different from the number of times the word appears!).

    ```python
    df = np.sum(word_counts > 0, axis=0)
    ```

5. Normalize the word count matrix to get the term frequencies. This means dividing each count by the L1 norm (the sum of all the counts). This makes each vector a vector of term frequencies.

    ```python
    tf_norm = word_counts.sum(axis=1)
    tf_norm[tf_norm == 0] = 1
    tf = word_counts / tf_norm.reshape(len(my_docs), 1)
    ```

6. Multiply the term frequency matrix by the log of the inverse of the document frequences to get the tf-idf matrix.

    ```python
    idf = np.log((len(my_docs) + 1.) / (1. + df)) + 1.
    tfidf = tf * idf
    ```

7. Normalize the tf-idf matrix as well by dividing by the l2 norm.

    ```python
    tfidf_norm = np.sqrt((tfidf ** 2).sum(axis=1))
    tfidf_norm[tfidf_norm == 0] = 1
    tfidf_normed = tfidf / tfidf_norm.reshape(len(my_docs), 1)
    ```

Using sklearn
=========================

1. Write the `tokenize` function. It should use nltk's `word_tokenize` as well as the stemmer or lemmatizer that you chose to use.

    ```python
    def tokenize(doc):
        '''
        INPUT: string
        OUTPUT: list of strings

        Tokenize and stem/lemmatize the document.
        '''
        return [snowball.stem(word) for word in word_tokenize(doc.lower())]
    ```

2. Apply the `CountVectorizer` on the whole corpus. Use your `tokenize` function from above. Do you get the same results as you did when you created this by hand?

    ```python
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

    countvect = CountVectorizer(stop_words='english', tokenizer=tokenize)
    count_vectorized = countvect.fit_transform(documents)
    ```

    Compare my results:
    ```python
    words = countvect.get_feature_names()
    print("sklearn count of 'dinner':", count_vectorized[0, words.index('dinner')])
    print("my count of 'dinner':", word_counts[0, vocab_dict['dinner']])
    ```

    *These are both 2.*

3. Apply the `TfidfVectorizer`.

    ```python
    tfidfvect = TfidfVectorizer(stop_words='english', tokenizer=tokenize)
    tfidf_vectorized = tfidfvect.fit_transform(documents)
    ```

    Compare my results:
    ```python
    words_tfidf = tfidfvect.get_feature_names()
    print("sklearn tfidf of 'dinner':", tfidf_vectorized[0, words_tfidf.index('dinner')])
    print("my tfidf of 'dinner':", tfidf[0, vocab_dict['dinner']])
    ```

Extra Credit 1: Cosine Similiarity using TFIDF
========================================================

Now that we're comfortable with tokenizing documents, let's use the cosine similarity to find similar documents.

1. Use sklearn's [linear_kernel](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html) to compute the cosine similarity between two documents.

    ```python
    from sklearn.metrics.pairwise import linear_kernel

    cosine_similarities = linear_kernel(tfidf_vectorized, tfidf_vectorized)
    ```

2. Now iterate over all possible pairs (as in 2 for loops iterating over the same list of documents) print the cosine similarities of their tfidf scores for each documents bag of words.

    ```python
    for i, doc1 in enumerate(docs):
        for j, doc2 in enumerate(docs):
            print(i, j, cosine_similarities[i, j])
    ```

Extra Credit 2: Part of speech tagging
========================================

As a side note, let's take a quick look at Part of speech tagging. These part of speech tags can be used as features.

You can see the documentation on the part of speech tagger in the [nltk book ch 5](http://www.nltk.org/book/ch05.html)

1. Since part of speech tagging takes a long time, pick off a single document.

2. Create a part of speech tagged version of the document. Which version of your documents should you use? The original tokenized one, the one with stop words removed, or the stemmed version? Try all of them and take a look at the results to see which one performs the best.

3. What happens if I part of speech tag my bag of words? Does it perform well? Why or why not?
