## Warmup: TF-IDF

**Include your code and answers in** `tfidf.py`.

#### Summarization

tf-idf can be applied to a document as very crude summarization. The basic approach is as follows:

* Split up a single description/document by sentence (essentially converting the single document to the corpus, with each sentence representing a "document")
* Apply the tf-idf weighting to each sentence. The term frequency becomes the freqency of a token in a sentence and the document frequency becomes the number of sentences a token appears in.
* Choose N sentences as the summarization.  Sentences can be selected based either on the highest total tf-idf weighting of its tokens, or the average tf-idf weighting of its tokens (why might these two be different and why do we care?). 

__Using the 20 newsgroups dataset__ (`sklearn.datasets.fetch_20newsgroups`)

We will be returning to the newsgroups dataset from [NLP day](https://github.com/gSchool/dsi-curriculum/blob/master/nlp/pair.md)

1. Summarize one article from each 20 newsgroup category into 2, 3, and 4 sentences and compare the results.  How do the summarizations of each topic differ?  Do your summarizations make sense for each article?
2. Summarize each topic as a whole. Return a paragraph (4-6 sentences) representing the most relevant sentences across a newsgroup topic.

**Hint:** Reuse your code from previous assignment to solve this faster.
