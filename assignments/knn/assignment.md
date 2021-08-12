## k-Nearest Neighbors

## Introduction
This algorithm is very simple to implement. Note that it takes nothing to train the model, you just need to save the data. When given a new data point, you need to calculate the distance of that data point to every existing data point and find the *k* closest ones.

## Basic

### Part 1: Generate Data

Use the code in `src/make_data.py` to generate some fake data. You
can run it like this:
```python
from src.make_data import make_data
X, y = make_data(n_features=2, n_pts=300, noise=0.1)
```

### Part 2: Implement kNN

**Include all your code for this section in** `src/knn.py`.

Here's the pseudocode for using k Nearest Neighbors to predict the value of a point `x`:

```
kNN:
    for every point in the dataset:
        calculate the distance between the point and x
        take the k points with the smallest distances to x (**hint: use numpy's argsort() function**)
        predict the value as the mean of the observed target values of these items
```

1. Implement the function `euclidean_distance` which computes the Euclidean distance between two numpy arrays.

2. Implement the class `KNNRegressor` in `src/knn.py`, with methods `fit`, `predict` and `__init__`. We are going to write our code similar to how sklearn does. You should be able to run your code like this:

    ```python
    knn = KNNRegressor(k=3, distance=euclidean_distance)
    knn.fit(X, y)
    y_pred = knn.predict(X)
    ```

    Here `X` is the feature matrix as a 2d numpy array, `y` is the values as a 1d numpy array. The 3 is the *k* and `euclidean_distance` is the distance function. `predict` will return a numpy array of the predicted labels.

3. Implement the function `cosine_distance` which computes a cosine-similarity-based metric between two numpy arrays. Specifically, use this formula:

    ![cosine distance](images/cosine_distance.png)

### Part 3: Explore results
1. Plot the values graphically. Use the code in `src/knn_visualization.py` to do this. Note that you'll need exactly 2 continuous features for it to work. Once you have tested it, change the `plot_predictions` function, adding an additional optional parameters to specify the name of the colormap, and test out a few different choices.

2. Test your algorithm on a dataset used for a previous exercise. Use [sklearn.metrics](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) to compute the mean-squared error of your model. Investigate how this depends on the value of `k`. Were the results what you expect? Talk about this with your neighbors.

## Advanced

### Part 4: Additional options
6. Add an additional option to your class to allow it to do a weighted mean, where the training points are weighted by the inverse of the distance to the point to be predicted, similar to the `weights='distance'` option in [`KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html).

7. Implement the `manhattan_distance` function. Compare the graphs produced with that, `euclidean_distance`, and `cosine_distance`. How are the graphs different?

## Extra Credit
### Part 3: Additional Practice

Practice with [recursion](https://github.com/GalvanizeDataScience/course-outline/tree/master/notes/reading_material/recursion).
