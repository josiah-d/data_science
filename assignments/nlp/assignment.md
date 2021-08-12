# NLP and Information Retrieval
- [NLP and Information Retrieval](#nlp-and-information-retrieval)
  - [Basic](#basic)
    - [Part 1: Setup](#part-1-setup)
    - [Part 2: Loading your data from Mongo](#part-2-loading-your-data-from-mongo)
    - [Part 3: Text Processing Pipeline](#part-3-text-processing-pipeline)
    - [Part 4: Tokenization and Stop words](#part-4-tokenization-and-stop-words)
    - [Part 5: Stemming/Lemmatization](#part-5-stemminglemmatization)
  - [Advanced](#advanced)
    - [Part 6: Bag Of Words and TFIDF](#part-6-bag-of-words-and-tfidf)
    - [Part 7: Using sklearn](#part-7-using-sklearn)
  - [Extra Credit](#extra-credit)
    - [Part 8: Cosine Similarity using TFIDF](#part-8-cosine-similarity-using-tfidf)
    - [Part 9: Part of speech tagging](#part-9-part-of-speech-tagging)
## Basic
### Part 1: Setup
> Expected time of completion: 15 mins.

![pipes](images/supervised_scikit_learn.png)

In this exercise, we'll be using MongoDB.  Make sure you start docker **and** your mongo container.

1. Start your container with:

    ```sh
    docker start mongoserver
    ```

    If the container with name `mongoserver` doesn't exist, it means you didn't complete this [assignment](https://github.com/GalvanizeDataScience/docker/blob/master/reference/docker_mongodb.md) earlier. Essentially, run the following command in your home directory, `~`.

    ```sh
    docker run --name mongoserver -p 27017:27017 -v "$PWD":/home/data -d mongo
    ```

2. After you've forked and cloned this repo, run:

    ```sh
    docker exec -it mongoserver bash
    ```

    This will enter a bash prompt within the mongoserver container

3. Within the container, navigate to where you cloned the repo. The filepath should end up being something like:

    ```sh
    home/data/your/filesystem/path/to/repo
    ```

4. The data is located in `data/articles_mongoimport.json`, so run the following command to create a new database (nyt_dump) with 1 collection (articles).

    ```
    mongoimport --db nyt_dump --collection articles  data/articles_mongoimport.json --batchSize 1
    ```

    (remove the `--batchSize 1` if you get any complaints)

5. As a sanity check, let's make sure the database loaded correctly.
    - Exit the bash prompt in the container
    
        ```
        exit
        ```
    - Enter a mongo prompt in the container

        ```
        docker exec -it mongoserver mongo
        ```
    - Check your local databases (you should see one called "nyt_dump")
    
        ```
        show dbs
        ```
    - To make sure the collection was created correctly as well (you should see one called "articles")
    
        ```
        use nyt_dump
        ```

        ```
        show collections
        ```
    - Pull one record to get a glimpse of what the data looks like and verify loading
        ```
        db.articles.findOne()
        ```

This data will be used throughout the exercise. We will be transforming the data set (documents) into a full bag of words that can be used for topic modeling and other advanced NLP techniques.

### Part 2: Loading your data from Mongo
> Expected time of completion: 10 mins.
1. After doing the above import, load all of the article content from the collection into a list of strings where each individual string is a NY Times article. 

    **Note:** the `"content"` field is a list of strings. You should just join these together, separated by white space.

    Here's one way to do it. For details, please refer to this previous [assignment](https://github.com/GalvanizeDataScience/docker/blob/master/reference/docker_mongodb.md).

    ```python
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    db = client.nyt_dump
    coll = db.articles

    documents = [' '.join(article['content']).lower() for article in coll.find()]
    ```

The content from each item in the collection, the parsed out article contents, should have no html or anything left. This will be our initial document set that we'll tokenize later on.

### Part 3: Text Processing Pipeline
> Expected time of completion: 5 mins.

**Goal:** Build a basic text processing pipeline to compare the documents. Let's play with nltk here. 

* Remember, a text processing pipeline involves tokenization, stripping stopwords, and stemming. 
* To use `nltk`'s built in tools, you may need to run

   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

### Part 4: Tokenization and Stop words
> Expected time of completion: 10 mins.
```python
from nltk.corpus import stopwords
```

1. Use nltk's [word_tokenize](http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.punkt.PunktLanguageVars.word_tokenize) to tokenize the documents.

    You should end up with a list of lists, like this:

    ```python
    [['this', 'is', 'the', 'first', 'document'], ['here', 'is', 'another', 'document']]
    ```

    Note: Don't forget to lowercase the strings!

2. Remove all the stop words. You should use nltk's stopwords (check out section 4.1 in [nltk book ch 2](http://www.nltk.org/book/ch02.html)).

    For best performance, make the stop words a set instead of a list.

### Part 5: Stemming/Lemmatization
> Expected time of completion: 20 mins.

Now that we have seen how to create a list of documents (lists of strings which are tokens), let's go through and stem / lemmatize each token. See [stemming](http://www.nltk.org/howto/stem.html) page and [lemmatization](http://www.nltk.org/_modules/nltk/stem/wordnet.html) page.

```python
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

porter = PorterStemmer()
snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()
```

1. Try running both stemmers and the lemmatizer on the documents. They only modify one word at a time, so you'll need to do a double for loop to apply the stemmer/lemmatizer to each word in all the documents.

    Save the results in 3 separate variables.

2. Compare the results. What do you notice are the differences between the two stemmers and the lemmatizer? Write your results as comments in your code!

3. Choose one of the 3 to use from here on out.

Note that using [part of speech tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging) will significantly increase the performance of lemmatization. You are encouraged to explore the differences on your own. This [stackoverflow question](https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk) provided some options you can try with. [Part 9: Part of speech tagging](#part-9-part-of-speech-tagging) also discussed this issue.


## Advanced
### Part 6: Bag Of Words and TFIDF
> Expected time of completion: 40 mins.

1. Create your vocab, a set of words UNIQUE over the whole corpus (list of documents which are lists of strings). A `set` is a good datatype for this since it doesn't allow duplicates. At the end you'll want to convert it to a list so that we can deal with our words in a consistent order.

    We call this the *bag of words*.

2. Create a reverse lookup for the vocab list. This is a dictionary whose keys are the words and values are the indices of the words (the word id). This will make things much faster than using the list `index` function.

3. Now let's create our word count vectors manually. Create a numpy matrix where each row corresponds to a document and each column a word. The value should be the count of the number of times that word appeared in that document.

4. Create the document frequencies. For each word, get a count of the number of documents the word appears in (different from the number of times the word appears!). Then divide that count by the total number of documents to get the document frequency.

5. Normalize the word count matrix to get the term frequencies. This means dividing each term count by the L1 norm (for a single document, this means the total number of words in that document). Now each value in a row represents the frequency of that term in that document.

6. Multiply the term frequency matrix by the log of the inverse of the document frequencies to get the tf-idf matrix.

7. Normalize the tf-idf matrix as well by dividing by the L2 (euclidean) norm.


### Part 7: Using sklearn
> Expected time of completion: flexible

Unsurprisingly, you don't actually have to do this by hand. You can use sklearn's [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) and [TFIDFVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

Here's what your code should look like:

```python
vect = CountVectorizer(stop_words='english')
word_counts = vect.fit_transform(documents)
```

  - `documents` here is a list of strings (not tokenized).
  - This also removes stop words.
  - Note that these vectorizers return the document-term matrix in a special [sparse matrix data type](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html). If you ever need to cast it to a numpy array, use the [`.toarray()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.toarray.html#scipy.sparse.csr_matrix.toarray) method
  

You can also use the same tokenization process that you did above by using the `tokenize` parameter, but you will need to write a `tokenize` function.

1. Write the `tokenize` function. It should use nltk's `word_tokenize` as well as the stemmer or lemmatizer that you chose to use.

    ```python
    def tokenize(doc):
        '''
        INPUT: string
        OUTPUT: list of strings

        Tokenize and stem/lemmatize the document.
        '''
    ```

2. Apply the `CountVectorizer` on the whole corpus. Use your `tokenize` function from above. Do you get the similar results as you did when you created this by hand?

    You can use `vect.get_feature_names()` to get the ids of the words.

3. Apply the `TfidfVectorizer`. Compare it to your tfidf results from above.

    Note: You may get slightly different values. Does sklearn follow the same normalization and smoothing operations you did above?


## Extra Credit
### Part 8: Cosine Similarity using TFIDF
> Expected time of completion: flexible

Now that we're comfortable with tokenizing documents, let's use the cosine similarity to find similar documents.

1. Use sklearn's [linear_kernel](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html) to compute the cosine similarity between two documents.

    Use the vectors created above with the tfidf vectorizer.

    Here's a page on cosine similarity from [sklearn documentation](http://scikit-learn.org/stable/modules/metrics.html#cosine-similarity) and a relevant [stack overflow post](http://stackoverflow.com/questions/12118720/python-tf-idf-cosine-to-find-document-similarity).

2. Now iterate over all possible pairs (as in 2 for loops iterating over the same list of documents) print the cosine similarities of their tfidf scores for each documents bag of words.

### Part 9: Part of speech tagging
> Expected time of completion: flexible

As a side note, let's take a quick look at Part of speech tagging. These part of speech tags can be used as features.

You can see the documentation on the part of speech tagger in the [nltk book ch 5](http://www.nltk.org/book/ch05.html)

1. Since part of speech tagging takes a long time, pick off a single document.

2. Create a part of speech tagged version of the document. Which version of your documents should you use? The original tokenized one, the one with stop words removed, or the stemmed version? Try all of them and take a look at the results to see which one performs the best.

3. What happens if I part of speech tag my bag of words? Does it perform well? Why or why not?
