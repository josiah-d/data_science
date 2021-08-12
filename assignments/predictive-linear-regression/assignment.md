## Linear Regression

## Introduction

This afternoon we will work through a linear regression problem from start to finish. 

You are given a dataset that contains information about 400 individuals' credit card and bank balances.
Your task is to predict an individual's balance based on various variables.

## Basic

### Part 1: Prepare data
 
1. Load the data into a dataframe from `data/balance.csv`. Make a scatter matrix of the variables. Comment on
   the distribution of your variables and describe the relationships between your numeric feature variables 
   and `Balance`.

2. Since `Gender`, `Married` and `Student` are boolean variables, convert the columns to `1/0`, i.e. the value should be `1` if the response to `Married` is `Yes`, otherwise `0`. 
   
3. Since `Ethnicity` is a categorical variable that has more than 2 categories, we need to convert the categories within the variable to separate columns with binary responses. These are known as dummy variables. Use `get_dummies` in pandas to get create dummy variables for `Ethnicity`. After you create the model, drop the `African` dummy variable. It can be any dummy variable you want the rest of the dummies to be compared against.  

### Part 2: Fit initial model

4. Using all the feature variables, fit a linear regression model to predict `Balance`. Validate the assumptions required of the linear regression model. Make a residual plot by plotting the fitted y values against the residuals. What do you observe?

5. The residuals should resemble a `v` shape. Try a few other models by excluding some features from the full model. Does the residual plot change?

   You should find that various `Balance` values are fitted around the `0` point. It would seem that the abundance of observations at `0` balance is affecting how the model is fit to the data. Plot the histogram for `Balance` again, except set `bins=100`. What do you observe?

6. In this scenario, the abundance of observations loaded at `0` are affecting the fit.  One option would be to fit more than one model.  In this case, our first "model" will predict 0 or non-zero balance based on just one feature. Later on we will look into more sophisticated models.  
    
   Re-plot the univariate scatter plot on a bigger figure size. Look for variable(s) that can differentiate most zero balance observation from non-zero balance observations. Use the provided pandas code as a reference.
   
   ```python
   df.plot(kind='scatter', y='Balance', x='Limit', edgecolor='none', figsize=(12, 5))
   ```

## Advanced

### Part 3: Two-part model
7. Once you find the relevant variable(s), decide on a threshold that would give you reasonable separation between the zero and non-zero observations, i.e. minimize false positive and false negative predictions. You can do it visually based on your plot now, but a slightly more sophisticated way to model this would be with a [Decision Tree](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor) which we will cover later in the course.  
   
8. Remove the data points below the decided threshold of your chosen variable and examine the number of zero observations that remain.  

   This is an atypical first step for linear regression but works well in this situation because we have a large loading of `0` observations in our response, which are affecting the regression fit.  In essence, we are fitting two models, one feeding into the other.  The first model simply predicts `0` or non-zero balance based on a single feature, the second model predicts the balance given that the first model predicted non-zero balance.  
   
9. Now re-fit the same model and examine the residuals. It might still be skewed, but should resemble more of a normal distribution.  While it's important to strive for models that pass the model diagnostic tests, in practice we sometimes loosen the restrictions a bit.  
   
10. Try out a few different models using different sets of features.  Later we will learn how to the correct way using LASSO regularization, but for now just try removing features that seem to have a small impact on the results. Note that the size of the coefficient won't tell you which features are important (why?).
 
## Extra Credit

### Part 4: Interactions, Polynomials, Transformations, etc.

11. Fit a linear model to predict `Balance` using `Income` as a predictor.  Fit a second model using `Income` and `Student` as predictors.  Finally fit a model using `Income`, `Student`, and `Income`*`Student` to account for a possible interaction    effect between Income and Student.  How do the models compare?  Is the interaction term significant?  

If the interaction term is significant, make a single plot with two regression lines, one for Student and one for non-Students.  You should have `Balance` on the y-axis, `Income` on the x-axis, and `Student` or non-`Student` coded in using two different colors (add a legend). 

You can compare the models using cross validation.
   
12. Return to your final model in  `10.`  Can you improve upon this fit by making transformations to your selected features?  

Generally, there is no defined end to the modeling process so this step can take as long as you would like, though if you have a small dataset you might overfit to the testing data.

