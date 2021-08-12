# Inferential Linear Regression

## Introduction

Linear regression is often used a predictive tool, and in this use case we don't need many statistical assumptions for it to do an admirable job.  Another common use for linear regression is *inferential*, and for this use case we need to check some statistical properties of the model.


There are two parts to this assignment.

  - The first part explores the assumptions of regression, and the tools available if these assumptions hold.
  - The second part explores the situations where linear regression fails.  This section requires some skill in using `numpy` to create example data.


## Basic
### Part 1: Assumptions for Inferential Regression

When using a linear regression to answer inferential questions, i.e. as a tool
to answer questions about some hypothetical *population* we need to make quite
a few assumptions about the data generating process (i.e. the population we are
studying with the regression). 

- **Independence of the observations.**
- **Constant Conditional Variance of Errors (Homoskedacity).**
- **Normal Distribution of Errors**

Since the inferential results (i.e. the standard errors of the parameter
estimates) of the regression model depend on these statistical assumptions, the
results of the regression model are only correct if our assumptions hold (at
least approximately).

**Note:**  The *predictions* of the linear regression model are not dependent on these assumptions, so if your goals are purely predictive, these assumptions are not strong concerns.

We will be exploring two datasets: `prestige` and `ccard`. Below is a description of the 2 datasets.

* `prestige`:
    - Target is the prestige of a job
    - Dependent variable: `prestige`.
    - Independent variables: `income`, `education`.  There are others, but you may feel free to exclude them for this exercise.

To load the prestige data set into a data frame:
  
  ```python
  import pandas as pd
  url = 'https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/carData/Duncan.csv'
  prestige = pd.read_csv(url)
  ```
   
* `ccard`
    - Target is average credit card expenditure.
    - Dependent variable: `AVGEXP`.
    - Independent variables: `AGE`, `INCOME`, `INCOMESQ`, `OWNRENT`.
  
To load the credit card data set into a data frame:

  ```python
  import statsmodels.api as sm
  credit_card = sm.datasets.ccard.load_pandas().data
  ```

1. Explore the datasets with a [scatter_matrix](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization-scatter-matrix) and a [boxplot](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#box-plots).
   
2. Fit a linear regression model to each of the datasets with `statsmodels`. Print and examine the
summaries of the models.  The summary should report the parameter estimates and
their standard errors.

3. Plot the residuals of the models against the predicted values.  Do these
residuals show any concerning patterns?  If so, how should you deal with them?
   
4. By inspecting the residual plots, which model is more likely to have
**heteroscedastic** residuals? Explain what heteroscedasticity means.

5. What uses of the model would heteroscedasticity (a violation of homoscedasticity) invalidate?

6. One of the most common treatments to reducing heteroscedasticity is to take
the logarithm of the response variable, especially if the conditional distribution of
the response variable is skewed. Take the log of `AVGEXP` in `ccard` data.
Re-fit the model to the logarithm of `AVGEXP`, and re-plot the residuals. 
   
7. To test if the residuals are normally distributed, the common practice is to
use a qq-plot (for quantile-quantile-plot). The Q-Q plot plots the quantile of
the normal distribution against that of the residuals and checks
for alignment of the quantiles.
    
Make qq-plots for the residuals of the `prestige` and `ccard` (before `log`
transform) models (it is assumed you will have to do a bit of research to make
these plots, we've intentionally omitted how to make them).  Apply the `log` transform to `AVGEXP` in
`ccard` and repeat the plot.  What do you observe?

8. The `p_values_` attribute of the model contains the results of applying a z-test to the parameter estimates.  Discuss the following questions with your partner:
  - What assumptions must hold for this z-test to be valid?
  - What is the null hypothesis of this z-test?
  - What is the distribution of the parameter estimates under the null hypothesis?


9. Give some examples of scientific questions that could be answered by these p-values.  Give some examples of questions that are *not* answered by these p-values.

10. Discuss with your partner or neighbor how you might calculate these p-values by hand.

## Advanced
### Part 2: A Failure Mode for Linear Regression

The least we could ask of a linear regression is that we can actually fit the model.  It turns out that linear regression has a simple failure mode that can be completely described.

1. Create a feature matrix `X` with two columns and 100 rows.  The first column should be an intercept column of all `1.0`'s, and the second should be randomly sampled from any distribution (a uniform is fine).

2. Create a target vector from a linear data generating process.  For example:

```
y = 1.0 + 2.0 * X[:, 1] + np.random.normal(size=100)
```

3. Fit a linear regression to `(X, y)` data.  Look at the fit coefficients (i.e. the *parameter estimates* in statistical language).  Are they what you expect them to be?  If you had fit the model to 1,000,000 data points, what would change about them? 

4. Create a new feature matrix `X` with three columns and 100 rows.  Make the first two columns the same as your previous `X`, but make the third column a *copy of the second column*, i.e., `X` should have the *same data* in the second and third column.

5. Fit a linear regression to the new `(X, y)` data (`y` should be the same as it was in the previous example).  What happened?

6. Hopefully you got an error, so there's something unfortunate going on here.
Think about what you think the correct answer should be, what coefficients *should* the model return?

7. Create a new feature matrix where one column is a multiple of another, and fit a linear regression again, what happened this time?  How can you explain it?

8. Create one last feature matrix where one column is a *linear combination* of two or more other columns.  Fit a linear regression using it.  What happened this time?  Can you explain it?

9. Hopefully you've seen a few linear regressions fail at this point.  Why did they fail?  What is the failure mode for linear regression?
