# Clustering
We're going to be talking about two clustering algorithms: K Means and Hierarchical. These algorithms are used to cluster similar data together. This is a form of *unsupervised learning*, meaning that we don't have a label or value to predict.

1. [K-means](#k-means)
2. [Hierarchical Clustering](#hierarchical-clustering)

## K-means
In the k-means algorithm, we create k clusters of our data. This is how the algorithm works:

```
Choose k random points to be the centroid of the k clusters.
Repeat until clusters stop changing:
    For every data point in the dataset, determine which centroid it is closest
        to and assign it to that cluster.
    Update the centroids to be the new center of all the points in that cluster
        (just take the arithmetic mean)
```

#### Calculating distance
We use Euclidean distance to calculate the closest centroid for each point:

![euclidean distance](images/euclidean_distance.png)

We can also think of it as a measure of the amount of variance within a cluster, so our goal is to minimize this variance.

#### Initializing the centroids
Every time you run K-means on the same dataset, you will not necessarily get the same clusters in the end. The clusters depend on the initial centroids!

In practice, we use an algorithm called K-means++ which is smarter about choosing the centroids. Here is the algorithm for choosing the centroids:

```
Choose one centroid at random.
Repeat until all centroids have been chosen:
    For each datapoint, compute the distance from x to all the centroids that
        have been chosen so far. Find the minimum distance, call it D(x).
    Choose the next centroid at random, using a weighted probability
        distribution where a point is chosen with probability proportional to
        D(x)^2.
```

This replaces the first step of the standard k-means algorithm.


## Hierarchical Clustering
A big drawback of k-means is that we have to choose k. How do we really know how many clusters our data should have? A different approach is hierarchical clustering.

Hierarchical clustering is a type of clustering algorithm where we build nested clusters. We represent this hierarchy as a tree or a dendrogram.

We end up with something like this:
![dendrogram](images/sortingDendrogram.png)

From a dendrogram, we can get different clusters by choosing a different break point.

Hierarchical clustering is more computationally expensive that k-means. Dendrograms also aren't useful if you have too much data to visualize.
