## SVD for Dimensionality Reduction

- [SVD for Dimensionality Reduction](#svd-for-dimensionality-reduction)
- [Introduction](#introduction)
  - [Dataset](#dataset)
  - [Task](#task)
- [Basic](#basic)
  - [Part 1: Prepare the data](#part-1-prepare-the-data)
  - [Part 2: Factor the Matrices](#part-2-factor-the-matrices)
    - [SVD](#svd)
- [Advanced](#advanced)
  - [Part 3: Examine the Topics](#part-3-examine-the-topics)
- [Extra Credit](#extra-credit)
  - [Part 4: Visualizing High-Dimensional Data](#part-4-visualizing-high-dimensional-data)
  - [Part 5: Interactive Plots](#part-5-interactive-plots)
## Introduction
There are a few techniques to actually perform the reduction.  In this portion of the sprint we will use Singular Value decomposition (SVD) to deconstruct a feature matrix and perform a dimensionality reduction.

### Dataset
We will be using a [book review](http://www2.informatik.uni-freiburg.de/~cziegler/BX/) dataset.  To make the matrix decomposition a little more tractable in the given time, the data files have already been joined and a sample of users and books have been taken.

There are 6100 books and 2500 users in the `data/book_reviews.csv`.  Each row corresponds to a given user's rating of a book.

### Task

The task of this assignment is to discover the latent features that determine readers' preference of books. You can also visualize these features in a low-dimensional space in the [Extra Credit](#extra-credit) part.

## Basic

### Part 1: Prepare the data
A common technique for both improving the quality of a recommendation as well as handling sparse data is matrix factorization.  We will be using Singular value decomposition ([SVD](http://en.wikipedia.org/wiki/Singular_value_decomposition)) to factor our reviews matrix.  This has the effect of reducing the dimension of our feature space and also uncovers latent features (similar to the topics from our document clustering): if we are talking about book reviews, latent features might correspond to given genres or styles.

1. Load in the `data/book_reviews.csv` data file to a dataframe.

2. Once the data is loaded we need to transform it into a feature matrix.  [Pivot](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot.html) the data such that each row represents a user, and each column (feature) represents their review of that book.  Represent missing data by a value of -1.

### Part 2: Factor the Matrices

#### SVD

Let us define:

* __m__: # of users
* __n__: # of items
* __k__: # of latent features (also rank of __A__)

We will be trying to decompose our rating matrix into 3 component matrices:

![http://www.shermanlab.com/science/CS/IR/DiracFockIR2/DiracFockRiemannAndIR_files/image002.gif](http://www.shermanlab.com/science/CS/IR/DiracFockIR2/DiracFockRiemannAndIR_files/image002.gif)

* **A** is our user-book rating matrix (__m__ x __n__)

    * **U** is our _weights_ matrix (__m__ x __k__)
    * **S** is our singular values matrix (__k__ x __k__)
    * and **V*** is our features matrix (__k__ x __n__)

The larger the singular value (**S** matrix), the more important that latent feature.  Since **U** and **V** are orthogonal to each other, we can rearrange them in order of decreasing singular values.  If we want to reduce the dimension, we simply set a threshold for which columns/rows to cut off (low rank approximation):

You can think of the weights matrix as representing how much of each latent feature corresponds to each user, and the features matrix as how much of each item/rating contributes to the latent features.

1. Using numpy's [SVD](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html) method, decompose our rating matrix into 3 component matrices.

    Now that we have our component matrices, we would like to inspect the decomposition and determine how many dimensions we should keep.  This is the same process as what we did this morning for the MNIST dataset with the scree-plot.

2. First calculate the power that each singular value represents.  Power is the same as variance of a dimension and we can compute it simply by squaring the singular values.

3.  Total power is the sum of the power of each singular value.  Plot the power of each singular value and look for the 'elbow'.  How many singular values should you keep?

4.  The reason we might be interested in total power is to have some sense of the information loss of our transformation.  Plot how the total power varies as you add additional singular values, i.e. plot total power of SV1<sup>2</sup>, SV1<sup>2</sup> + SV2<sup>2</sup>, SV1<sup>2</sup> + SV2<sup>2</sup> + SV3<sup>2</sup>, etc.  This is equivalent to the cumulative sum of the squares of the singular values.

5.  How many singular values do you need to keep to retain 90% of the total power?

 ## Advanced

### Part 3: Examine the Topics

 Now that we have decomposed our matrices, let us try to examine the 'concept/topic' space.  Each row of U connects users to concepts, and each row of V<sup>T</sup> connects concepts to books.  Examine U and V<sup>T</sup>.

6. Pick a number of singular values to keep (you'll be evaluating latent topics by eye, so keep it to 10 or so).  Look at V to find which books most contribute to each 'topic'.  For each of these 'topics', print out the title and author of the 10 most relevant books.  __Note: You can get the book metadata from the `data/book_meta.csv` file__  Use:

      ```python
      meta_data = pd.read_csv('data/book_meta.csv', sep=";", error_bad_lines=False, encoding='latin1')
      ```

7. What does each concept represent?  Can you give them names based on which books comprise them?

8. Do the same for the users.  How much of each concept does the first user like?

We will leave this data set for now, but when we get to recommenders we will already have this exploration and transformation under our belt.

## Extra Credit

### Part 4: Visualizing High-Dimensional Data

We have touched on many of the issues and treatments of dealing with data that has many dimensions for modeling purposes.  This last section will focus on trying to better understand our data through visualization.  One technique that is often employed to visualize data of arbitrary dimensions is [Multidimensional Scaling](http://en.wikipedia.org/wiki/Multidimensional_scaling) (MDS).  The basic idea of MDS is to compute similarity in an arbitrarily high dimension (the dimension of your original data) and project this into a two dimensional space in a way to preserve distances.  Basically the points in 2-D space should have the same distances between them as they had in the higher dimensional space.

One classic application of MDS is to visualize voting patterns in the senate.  This is probably so because people love betting on bills like they bet on horse races, but also the senate is a classic example of a partisan 'user base'. We will be working with data from [Vote View](http://www.voteview.com/) and the data dictionary of the structure can be found [here](http://www.voteview.com/senate101.htm).  We will be looking at the Senate votes from the 101-111th senates (1989-2009). Each row of the data corresponds to a single senator and his/her votes for that session of the senate.

Lets see if we can discover anything interesting in the way our senators voted in the 90s!

1.  Load in the data from `data/senate/*`, making one data frame for each session (you could store these data frames in a dictionary, or make one large dataframe and add another index for session).

2. Now that we have our data in a form that is easy to manipulate we need to convert the voting codes.  They are currently on a more complex 0-9 scale, but we should put them on a Yay (1), Nay (-1), abstain (0) scale.  Map every vote accordingly:
  * 1,2,3 -> 1
  * 4,5,6 -> -1
  * 7,8,9,0 -> 0

 While scikit-learn's [MDS](http://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html) can precompute distances for us, it is unfortunately only limited to Euclidean distance.  It does however let us precompute our own distance calculation.

3. We are now ready to compute our distances.  Let us first start with the 101st session for now.  Extract all rows that correspond to the 101 Senate and using scipy's [pdist](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html) create a similarity matrix of our senators.  Start with Euclidean for now.
4. Pass this matrix into scikit's [MDS](http://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html) to compute the scaling (remember to tell it you precomputed the distances).
5. Plot our senators in 2-D space.  Start with just points colored blue and red accordingly, but then see if you can instead plot their names so we know who is aligned where.

 ![mds](images/101MDS.png)

6. Now repeat this for all of the senates in our dataset and track the evolution of partisanship in the Senate!
 ![all](images/allMDS.png)

7. Try to experiment with different distance metrics and see if the plot you created change.
8. Also, try to visualize the data according to its first two principal components and plot them in a similar manner.  Does MDS give a different picture than PCA?

### Part 5: Interactive Plots

1. Instead of awkwardly visualizing our data points as the senators names, we can get the best of both worlds (interpretability and inspection) through interactivity! Using [plotly](https://plot.ly/python/) create the same [scatterplot](https://plot.ly/python/line-and-scatter/#Colored-and-Styled-Scatter-Plot) but with a hover interaction so the senators name (and other info) pops up in the tooltip. Plotly kinda defaults to this and gives it to us for free.
