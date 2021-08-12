# Boosting Implementation
- [Boosting Implementation](#boosting-implementation)
    - [Hints:](#hints)
  - [Basic](#basic)
    - [Part 1: Implement basic boosting model](#part-1-implement-basic-boosting-model)
    - [Part 2: Add hyperparameters](#part-2-add-hyperparameters)
  - [Advanced](#advanced)
    - [Part 3: Mean-absolute-error (`mae`) loss](#part-3-mean-absolute-error-mae-loss)
    - [Part 4: Test using other estimators](#part-4-test-using-other-estimators)
  - [Extra credit](#extra-credit)
    - [Part 5: Sklearn estimators](#part-5-sklearn-estimators)

This assignment will have us develop a gradient boosted regressor using Decision Tree models from `sklearn`, to help us understand the how the algorithm works.

### Hints:
1. Try to google new concepts and read the sklearn documentation to understand them. For example `DummyRegressor` is mentioned without background information. You need to google and learn how to use it.

## Basic
### Part 1: Implement basic boosting model

Write code (in `src/boosting.py`) to implement a gradient-boosted regressor.

1. Load the boston data set into a notebook and do a train-test split. Import the existing stub class. Instantiate it and fit and predict on the data, confirming it does what you expect (i.e., nothing). After each subsequent step, fit and predict on the results, and verify you are getting the results you expect.

2. Implement the `__init__` method, for now adding `n_estimators` and `learning_rate` as the only other parameters. Set matching attributes, and an attribute (a list) with the estimators.

3. Begin implementing the `fit` method, creating just the first estimator and add it to the list. The first estimator should predict the mean of the y values used to fit it (you can use `DummyRegressor`).

4. Implement the `predict` method. It should return the total prediction of all the estimators (even though right now you only have one).

5. Finish the `fit` method. After creating the first estimator, do `self.n_estimators` times:
    a. Predict on the training data over the previous estimators,
    b. Subtract those predictions from the training targets, and multiply by the learning rate,
    c. Create a new estimator (using a `DecisionTreeRegressor` from `sklearn`) using the **above** as a target, and
    d. Append the estimator to the list.

6. Calculate the mean-squared error on the test data for a one, five, twenty, and 100 estimators using a 0.1 learning rate. Check the error occasionally on later steps.

Note that this is **not** how you would ordinarily find the best value for n_estimators when using gradient boosting. A model fit to 100 estimators could be written to predict with any smaller number of estimators (staged predict in sklearn) but we aren't implementing that.

### Part 2: Add hyperparameters

1. Add a `subsample` parameter to `__init__`, specifying the fraction of data points to include in each step. Use a reasonable default, using the principles that the default value should be a) the best choice to use most of the time and b) the simplest option, and c) consistent with other code. Discuss your choice of default with your neighbor.

2. Most of the hyperparameters generally used with boosted trees are hyperparameters of the underlying estimators (e.g., `max_depth`). While we could include these individually and it would let us verify them better, it's quicker and easier to allow arbitrary named parameters.

Add a `**kwargs` parameter to the `__init__` method. Save any such arguments as attributes and pass them as arguments to the `DecisionTreeRegressor` using the `**` syntax.

## Advanced

### Part 3: Mean-absolute-error (`mae`) loss

The code above uses the mean-squared error as a loss function. The derivative of this loss function with respect to the prediction at a single point is simply the residual itself.

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Cmathcal%7BL%7D%20%3D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7Bi%3D0%7D%5EN%20r_i%5E2"></div>

where <!-- $r_i$ --> <img src="https://render.githubusercontent.com/render/math?math=r_i"> is the residual <!-- $y_i - \bar{y}_i$ --> <img src="https://render.githubusercontent.com/render/math?math=y_i%20-%20%5Cbar%7By%7D_i">. So

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Cfrac%7B%5Cpartial%20%5Cmathcal%7BL%7D%20%7D%7B%5Cpartial%20r_i%7D%20%3D%20%5Cfrac%7B1%7D%7BN%7D%202r_i"></div>

We're then fitting next model by some constant times the residuals (we can treat the <!-- $2 \over N$ --> <img src="https://render.githubusercontent.com/render/math?math=2%20%5Cover%20N"> constant as part of the learning rate).

Suppose we use the mean of absolute values of the residuals as a loss function instead.

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=%5Cmathcal%7BL%7D%20%3D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7Bi%3D0%7D%5EN%20%7Cr_i%7C"></div>

1. What is the derivative of the loss function with respect to each of the residuals? How should we change the gradient step to account for the different loss function? Discuss this with other students or instructors to make sure you understand before proceeding.

2. Add an optional paramenter to `__init__` specififying the loss function. If it has a value of `mae`, use the alternate loss function.

3. Test out the result on some fake data with outliers:
```python
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
npts = 500
noutliners = 10
xfake = stats.uniform(0, 10).rvs(npts)
yfake = np.sin(xfake) + stats.norm(0, 0.5).rvs(npts)
yfake[:noutliners] = 20
```
Make of a graph of the predictions with the original model and the MAE version. How do they compare? Hint: use a large number of points in the graph to capture any spikes around outliers.

### Part 4: Test using other estimators

1. Add a parameter to `__init__` representing the underlying estimator. It should expect a class (with a default value of `DecisionTreeRegressor`). Save that as an attribute, and use that to create the estimators rather than `DecisionTreeRegressor`.

2. Test the results the code using `LinearRegression`. Compare the predictions to those from those with `LinearRegression` alone. Are the results what you expect? Why?

3. Test the results with `KNeighborsRegressor`.  Compare the predictions to those from those with `KNeighborsRegressor` alone. Are the results what you expect? Why?


## Extra credit

### Part 5: Sklearn estimators

Look at he [documentation](https://scikit-learn.org/stable/developers/develop.html) for developing estimators for `sklearn`. Update your code to follow the guidelines.

