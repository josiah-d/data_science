# Regularized Regression

## Introduction

In this assignment we will be comparing regularization methods on a well known dataset that is built into sklearn.

## Basic
### Part 1: Loading The Data

We're going to use a classic regression dataset for this example.

1. Load the diabetes data from sklearn using the instructions in the [sklearn documentation](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html).

2. Some of the work at the end of this assignment will be very computationally heavy, so we will subset our data to make this work more approachable.  Take the first 100 rows from the diabetes data and target to use as your raw data in this assignment.

3. Take an initial look at the data and investigate what the predictors mean.  You may have to do some detective work with google.

4. Do some basic EDA.  Check for missing values, and plot the univariate and joint distributions of the predictors and target.  Make any sensible changes to the data based on what you discover in your explorations.

## Part 2: Ridge Regression

Ridge regularization is a form of *shrinkage*: the parameter estimates are shrunk towards zero compared to the estimates from an unregularized regression. The amount of regularization (i.e. the severity of the shrinkage) is set via the `alpha` parameter of `Ridge`, which needs to be tuned with cross-validation. 

There is a `RidgeCV` class in sklearn which can automate some of the work involved in tuning alpha, but today we will do this manually to get our hands dirty.

1. Split the full data into a training and testing set.  The training set will be used to fit and tune all of your models, and the testing set will be used only at the very end to compare your very final models.

2. Let's fit a model just to get the mechanics of using `Ridge` down.  Fit a ridge regression with `alpha = 0.5` to your training dataset.  Use the fit model to generate predictions on your testing dataset.  Calculate the MSE of your fit model on the test set.  

3. Estimate the out of sample error of your ridge regression using 10-fold cross validation.  Remember that your predictors and response **must** be standardized when using ridge regression, and that this standardization must happen **inside** of the cross validation using **only** the training set!  Your code should look something like this:

```python
kf = KFold(n_splits=n_folds, random_state=random_seed)
test_cv_errors, train_cv_errors = np.empty(n_folds), np.empty(n_folds)
for idx, (train, test) in enumerate(kf.split(X_train)):
    # Split into train and test
    ...
    # Standardize data, fit on training set, transform training and test.
    ...
    # Fit ridge regression to training data.
    ...
    # Make predictions.
    ...
    # Calculate MSE.
    ...
    # Record the MSE in a numpy array.
    ...
```

To make the task of standardizing both the predictor and response more seamless, we have provided an `XyScaler` class in `utils.py`.

**Nota bene**: Why standardize the response variable `y`? Normally we would leave
`y` as it is, but sklearn's StandardScaler also standardizes the intercept which 
is not technically correct: see [here.](https://stats.stackexchange.com/a/161689) 
Standardizing `y` corrects for this deficiency.

However, there is a disadvantage to scaling your response in terms of interpretability
of the coefficients.  A worthwhile investigation would be to compare results with
and without scaling your response and see if you get drastically different performance
results in cross-validation.

4. Wrap your cross validation code from above into a function:

```python
def cv(X, y, base_estimator, n_folds, random_seed=154):
    """Estimate the in- and out-of-sample error of a model using cross
    validation.
    
    Parameters
    ----------
    
    X: np.array
      Matrix of predictors.
      
    y: np.array
      Target array.
      
    base_estimator: sklearn model object.
      The estimator to fit.  Must have fit and predict methods.
      
    n_folds: int
      The number of folds in the cross validation.
      
    random_seed: int
      A seed for the random number generator, for repeatability.
    
    Returns
    -------
      
    train_cv_errors, test_cv_errors: tuple of arrays
      The training and testing errors for each fold of cross validation.
    """
```

5. Vary the values of alpha starting at zero. Compute the training and testing errors for each value of alpha using ten-fold cross validation.

To do this, it's best to write another function:

```python
def train_at_various_alphas(X, y, model, alphas, n_folds=10, **kwargs):
    """Train a regularized regression model using cross validation at various
    values of alpha.
    
    Parameters
    ----------
    
    X: np.array
      Matrix of predictors.
      
    y: np.array
      Target array.
      
    model: sklearn model class
      A class in sklearn that can be used to create a regularized regression
      object.  Options are `Ridge` and `Lasso`.
      
    alphas: numpy array
      An array of regularization parameters.
      
    n_folds: int
      Number of cross validation folds.
      
    Returns
    -------
    
    cv_errors_train, cv_errors_test: tuple of DataFrame
      DataFrames containing the training and testing errors for each value of
      alpha and each cross validation fold.  Each row represents a CV fold, and
      each column a value of alpha.
    """
    cv_errors_train = pd.DataFrame(np.empty(shape=(n_folds, len(alphas))),
                                     columns=alphas)
    cv_errors_test = pd.DataFrame(np.empty(shape=(n_folds, len(alphas))),
                                        columns=alphas)
    for alpha in alphas:
       # ...
    return cv_errors_train, cv_errors_test
```

Which you can call like this:

```python
ridge_alphas = np.logspace(-2, 4, num=250)

ridge_cv_errors_train, ridge_cv_errors_test = train_at_various_alphas(
    X_train, y_train, Ridge, ridge_alphas)
```

6. Average your ten estimates of training and testing error for each alpha to get a more stable estimate of the training and testing error for each value of the regularization parameter. Plot the average training and testing MSE curves as alpha varies (the plot will look better if you use log(\alpha) on the horizontal axis).  

7. Compute the value of alpha that leads to the minimum CV test error, then superimpose a vertical line at the optimal value of alpha onto your plot of the MSE curves.

8. Fit a sequence of ridge regression models to the full training data for the same sequence of alpha's as above, then plot the coefficient paths as a function of log(alpha).  Superimpose a vertical line at the optimal value of alpha as chosen by cross validation.

## Advanced

### Part 3: Lasso

**LASSO Regression** is useful for imposing sparsity on the coefficients. In
other words, it is preferred if we believe many of the features are not at all relevant to predicting the target.

Repeat the sequence you followed for `Ridge`, but using the `Lasso` class from sklearn.  You will need to use a different sequence of alpha values for good results.

### Part 4: Model Comparison

1. Fit a final ridge regression and LASSO regression to your full training set using the values of alpha you found as optimal using cross validation.  Compute the MSE of these models on your held out test set (this should be the first time you have used the test data for anything).

For comparison, also fit an unregularized linear regression on the training data and compute it's MSE on the test set.

2. Given this information, which model would you choose as final?  What next steps would you take before putting it into production?

## Extra Credit
### Part 5: Quantifying Variation

You probably noticed that the results from our final comparison of three models is too close to call. The bootstrap is a useful tool in these situations.

The idea in using the bootstrap here is to wrap our *entire process* in an outer bootstrap loop.  So we would:

  - Begin by taking a bootstrap sample from our entire dataset
  - Then split this bootsrap sample into training and testing sets
  - Then use ten fold CV on the training set to estimate an optimal regularization parameter
  - Then refit the model on the entire training set using this optimal parameter
  - Then score the resulting model on the held out test set

This process is repeated many times for different bootstrap samples of the data.  After it is completed, we will have an array of estimates of the testing error for our process, which we can compare for different models (say comparing ridge vs. lasso regression).  This will help us choose without the fear that we chose a train-test split that benefits one or the other model.

```python
def booststrap_cv(X, y, model, alphas, n_bootstraps=100, n_folds=10, **kwargs):
    test_errors = np.empty(n_bootstraps)
    for idx in range(n_bootstraps):
        X_boot, y_boot = resample(X, y)
	# Split into train and test
	# ...
	# Fit a range of models with cross validation on the train data
	# ...
	# Compute the optimal alpha using the CV estimates
	# ...
	# Fit the model with optimal alpha to the entire training data
	# ...
	# Calculate the MSE of the final model using the test data
	# ...
    return test_errors
```

Fill in the code for this function and bootstrap your process for both ridge and LASSO regression.  Then plot a histogram of the bootstrapped test MSE's to determine which regression method is better for this data.

Use a small number of bootstrap samples for now, as this is a very compute intensive process.  For definitive results, run it with 10000 bootstrap samples overnight.  If you do so, **make sure your computer is plugged into a power source!**

You may also wish to re-run your analysis on the **full** diabetes data, you may find some interesting results!
