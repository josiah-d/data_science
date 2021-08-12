Natural Language Processing
===

This exercise continues our journey into Natural Language Processing.  As you may have noticed, text is very different from numbers, which both are very different from images, and users, and.... Moral of the story, every type of data is unique and has its own set of challenges.  We need to encode (quantize) all of these so that we can apply our ML theory to build models and the more effectively we can encode their context/meaning, the more powerful our model will be.  Once quantized (in a matrix) it doesn't matter (as much) what type our data originated as, we can then apply our ML machinery/models transparently.

Today will focus on how to effectively capture the richness of human language in a numeric/matrix form.

### Resources

* [OG presentation on NLTK](http://www.slideshare.net/ogrisel/statistical-machine-learning-for-text-classification-with-scikitlearn-and-nltk)
* [NLTK book](http://nltk.org/book/)
* [One Page tf-idf tutorial](http://www.tfidf.com/)
* [Finding important words with TF-IDF](http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/)

#### [Text Feature Selection](http://nlp.stanford.edu/IR-book/html/htmledition/feature-selection-1.html)
* CPT Tables (Naive Bayes): Look at your model's CPT tables to find word importances for a class
* [Chi-Squared](http://nlp.stanford.edu/IR-book/html/htmledition/feature-selectionchi2-feature-selection-1.html)
* [Mutual Information](http://nlp.stanford.edu/IR-book/html/htmledition/mutual-information-1.html)
* [Pointwise Mutual Information](http://stackoverflow.com/questions/13488817/pointwise-mutual-information-on-text)

#### Feature engineering
* [N-Grams](http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/)
* [Hashing Trick](http://blog.someben.com/2013/01/hashing-lang/)
* [Feature Hashing](http://en.wikipedia.org/wiki/Feature_hashing)
* [Normalization/Feature Scaling](http://en.wikipedia.org/wiki/Feature_scaling)
* Handcrafted Features: incorporate meta-data (author, date, total word count, etc.), include sentiment, domain knowledge, etc.

#### [Vector Space Model](http://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html) (and similarity)
* [Cosine Similarity](http://nlp.stanford.edu/IR-book/html/htmledition/dot-products-1.html)
