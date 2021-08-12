# Clustering
- [Clustering](#clustering)
  - [Introduction](#introduction)
  - [Basic](#basic)
    - [Part 1: Find initial clusters](#part-1-find-initial-clusters)
    - [Part 2: Investigate the clusters](#part-2-investigate-the-clusters)
  - [Advanced](#advanced)
    - [Part 3: Hierarchical Clustering](#part-3-hierarchical-clustering)
    - [Part 4: Hierarchical Topics](#part-4-hierarchical-topics)
  - [Extra Credit](#extra-credit)
    - [Part 5: Selecting `K` utillizing Silhouette analysis](#part-5-selecting-k-utillizing-silhouette-analysis)
    - [Part 6: Congressional voting](#part-6-congressional-voting)
## Introduction
K-means' centroids represent the average or typical observation in each cluster, and examining the centroids can shed light on the essential traits or identity of each observation. For example, k-means applied to the MNIST digit dataset reveals the "average" digits:
![images](images/images.png)

Applying K-means to TF-IDF or bag-of-words features produces topic centroids. For this sprint, you will perform topic modeling on news articles using k-means and hierarchical clustering. You may refer to the references in the [`reference`](reference) directory for examples.

## Basic

### Part 1: Find initial clusters
> Expected time of completion: 20 mins.

The repo contains a 'articles.csv' file that has 1405 articles from 'Arts','Books','Business Day', 'Magazine', 'Opinion', 'Real Estate', 'Sports', 'Travel', 'U.S.', and 'World'.

1.  Load the articles in `articles.csv` using pandas' `pd.read_csv()`.  Use `TfidfVectorizer` to vectorize the `content` fields of the articles. Please pay attention to the `encoding`.

    ```python
    articles_df = pd.read_csv("data/articles.csv", encoding="utf-8")
    ```

2. Apply Kmeans clustering to the resulting data with [scikit-learn's](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) module.
    > hint: You may need to use the following line to avoid this [error](https://stackoverflow.com/questions/39303912/tfidfvectorizer-in-scikit-learn-valueerror-np-nan-is-an-invalid-document).

    ```python
    X = vectorizer.fit_transform(articles_df['content'].values.astype('U'))
    ```

### Part 2: Investigate the clusters  
> Expected time of completion: 45 mins.

3. To find out what "topics" Kmeans has discovered we must inspect the centroids.  Print out the centroids of the Kmeans clustering.
   
   These centroids are simply a bunch of vectors.  To make any sense of them we need to map these vectors back into our 'word space'.  Think of each feature/dimension of the centroid vector as representing the "average" article or the average occurrences of words for that cluster.

4. But for topics we are only really interested in the most present words, i.e. features/dimensions with the greatest representation in the centroid.  Print out the top ten words for each centroid.
  * Sort each centroid vector to find the top 10 features
  * Go back to your vectorizer object to find out what words each of these features corresponds to.

4. Look at the docs for `TfidfVectorizer` and see if you can limit the number of features (words) included in the feature matrix.  This can help reduce some noise and make the centroids slightly more sensible.  Limit the `max_features` and see if the words of the topics change at all.

5. An alternative to finding out what each cluster represents is to look at the articles that are assigned to it.  Print out the titles of a random sample of the articles assigned to each cluster to get a sense of the topic.

6. What 'topics' has Kmeans discovered? Can you try to assign a name to each?  Do the topics change as you change k (just try this for a few different values of k)?

7. If you set k == to the number of NYT sections in the dataset, does it return topics that map to a section?  Why or why not?

8. Try your clustering only with a subset of the original sections.  Do the topics change or get more specific if you only use 3 sections (i.e. Sports, Art, and Business)?  Are there any cross section topics (i.e. a Sports article that talks about the economics of a baseball team) you can find? 

## Advanced

### Part 3: Hierarchical Clustering
> Expected time of completion: 50 mins.

![dendrogram](images/sortingDendrogram.png)

We have been introduced to distance metrics and the idea of similarity, but we will take a deeper dive here. For many machine learning algorithms, the idea of 'distance' between two points is a crucial abstraction to perform analysis. For Kmeans we are usually limited to use Euclidean distance even though our domain might have a more appropriate distance function (i.e. Cosine similarity for text).  With Hierarchical clustering we will not be limited in this way.   
We already have our bags and played around with Kmeans clustering.  Now we are going to leverage [Scipy](http://www.scipy.org/) to perform [hierarchical clustering](http://en.wikipedia.org/wiki/Hierarchical_clustering).

__Note: [Here](http://nbviewer.ipython.org/github/herrfz/dataanalysis/blob/master/week3/hierarchical_clustering.ipynb) is a very simple example of putting all of the pieces in this part together.__



1. Hierarchical clustering is more computationally intensive than Kmeans.  Also it is hard to visualize the results of a hierarchical clustering if you have too much data (since it represents its clusters as a tree). Create a **subset** of the original articles by filtering the data set to contain at least one article from each section and at most around 100 total articles. **Please be aware the possibility of empty articles. Do make sure the `contents` field is not NaN. Otherwise you will run into this [problem](https://github.com/scikit-learn/scikit-learn/issues/7689).**

    > One issue with text (especially when visualizing/clustering) is high dimensionality.  Any method that uses distance metrics is susceptible to the [curse of dimensionality](http://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/).

2. The first step to using `scipy's` Hierarchical clustering is to first find out how similar our vectors are to one another.  To do this we use the `pdist` [function](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html) to compute a similarity matrix of our data (pairwise distances).  First we will use `cosine` distance.  Examine the shape of what is returned.

    ```python
    distances = pdist(small_X.todense(), metric='Cosine') # small_X is the subset
    ```

3. A quirk of `pdist` is that it returns one looong vector.  Use scipy's [squareform](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html) function to get our long vector of distances back into a square matrix.  Look at the shape of this new matrix.
   > Hint: The matrix is going to be a square matrix.

4. Now that we have a square similarity matrix we can start to cluster!  Pass this matrix into scipy's `linkage` [function](http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html) to compute our hierarchical clusters.

5. We in theory have all the information about our clusters but it is basically impossible to interpret in a sensible manner.  Thankfully scipy also has a function to visualize this madness.  Using scipy's `dendrogram` [function](http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html) plot the linkages as a hierachical tree.

### Part 4: Hierarchical Topics

> Expected time of completion: flexible.

Now that we have our dendrogram we can begin exploring the clusters it has made.

1. To make your clusters more interpretable, change the labels on the data to be the titles of the articles. Can you find any interesting clusters or discover any topics not present in the NYT sections?  Are there any overlaps with the Kmeans topics and the hierarchical topics?

2. In addition, we might also be interested in how these hierarchical clusters compare to the NYT sections.  Label each point not only with the title but also the NYT section it belongs to.  Do any cross section topics emerge?

    __Protip: You can output a hi-res [image](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig) with matplotlib to then view outside of IPython (which you can zoom in on).__

    ![articles.png](images/article_cluster.png)

3. Explore different clusterings on a per section basis. Perform the same analysis on each of the Arts, Books, and Movies sections (i.e. cluster one section at a time).

4. Repeat this process using Euclidean distance (and if you have time, Pearson correlation and the Jaccard distance).  Read about scipys distance metrics [here](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html#scipy.spatial.distance.pdist).  Why might cosine distance be better for clustering the words of our articles?

5. Compare the clusters returned with cosine and Euclidean distance metrics.

6. We have visualized similarity between articles, but we can also see which words are similar and co-occur.  This dendrogram is somewhat less-sensical, but let's look at it anyway.  First limit the number of features with the vectorizer (if you haven't already).  500-1000 words is probably the limit of what you can visualize effectively.  Transpose your feature matrix so now rows correspond to words and the columns correspond to the articles.

7. Perform the same analysis as above and inspect the dendrogram with the words from the articles.  Anything you wouldn't expect?

    ![words.png](images/words_cluster.png)

## Extra Credit

> Expected time of completion: flexible.

Note that there is no solution provided for the extra credit parts.


### Part 5: Selecting `K` utillizing Silhouette analysis

Refer to the implementation of [silhouette score](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html) in scikit-learn and revisit [Part 2: Investigate the clusters](#part-2-investigate-the-clusters) to determine the optimal `K` value for clustering.

### Part 6: Congressional voting

There is a [congress.csv](data/congress.csv) file. Try to discover user segments/demographics from the dataset.

1. Apply both kmeans and hierarchical clustering to the datasets.  Do any meaningful clusters come out from either?
2. What are the characteristics of the user groups from Kmeans (i.e. the 'average' user from each group)?
3. Try to change the value of k and inspect the clusters.
4. A benefit of hierarchical clustering is that there is no need to set k.  Using the clusters returned from hierarchical clusters, try to intuit a good value of k.
5. Run Kmeans with this value.  Do the clusters come out to be similar to the hierarchical clusters?
