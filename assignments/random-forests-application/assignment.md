# Random Forests with sklearn

## Introduction

In this sprint we will be practicing using the `scikit-learn` implementation of random forests. For this exercise, we'll be attempting to classify whether a customer churns or not given a set of inputs. We can use the Random Forest to get more insight into the churn data. Only about 15% of the data points are positive for churn. 

The documentation for sklearn's random forest can be found here: [RandomForestClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

You might find the documentation for these sklearn functions helpful: [precision_score](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html), [recall_score](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html) and [confusion_matrix](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html).

## Basic

### Part 1: Prepare data

Each row represents a subscribing telephone customer. Each column contains customer attributes such as phone number, call minutes used during different times of day, charges incurred for services, lifetime account duration, and whether or not the customer is still a customer.

1. Load the `data/churn.csv` file into a pandas DataFrame.

1. Convert the "no", "yes" values to booleans (True/False) as well as any booleans that are stored as strings.

1. Remove the features which aren't boolean or meaningfully numerical.

1. Make a numpy array called `y` containing the churn values.

1. Make a 2-dimensional numpy array containing the feature data (everything except the labels) called `X`.

1. Use sklearn's `train_test_split` to split into train and test set.

### Part 2: Train a model

1. Use sklearn's `RandomForestClassifier` to build a model of your data. Start by using the defaults for all of the parameters.

1. What is the accuracy score on the test data?

1. Draw a [confusion matrix](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) for the results.

1. What are the precision and recall?

1. Build the `RandomForestClassifier` again setting the out of bag parameter -- `oob_score` to be `True`. Compare the out of bag score of the *training* set with the accuracy on the *test* set. How close are they?

    It might complain that you are using too few trees to reliably use out of bag score. You can still see the results, but try increasing the number of trees as well to remove the warning.

1. Say you would like to give advice for what to focus on to prevent churn. You would like to be able to say what specifics about a user you should focus on changing in order to make them not churn. Use sklearn's model to get the feature importances. What are the top five features? What could you do to potentially limit churn?

## Advanced

### Part 3: Optimize the result
1. Try modifying the number of trees. The default is 100 trees. Try 5-10 different values for the number of trees and make a graph of the number of trees versus the accuracy score. Is there a point where creating more trees doesn't seem to help anymore?

    If you get an inconsistent graph, try creating a few random forests for each number and averaging the accuracies. This should smooth out your graph.

1. Try modifying the max features parameter. For the `RandomForestClassifier`, the default value is `sqrt(total # of features)` (whereas the `RandomForestRegressor` default is `total # of features`). Try all the different possible values (1 to the total number of features) and make a graph of the number of features versus the accuracy score. Is there a point where using additional features doesn't seem to help? For a more in-depth discussion on the choice of `max_features` in a random forest, see the discussion [here](https://stats.stackexchange.com/a/324382).

1. Run all the other classifiers that we have learned so far in class (logistic regression, decision tree, k nearest neighbors) using sklearn's default parameters for all of them. You can use the optimal parameters you found above for Random Forest. If you have time, you can tune the other models as well. Which gets the highest accuracy? Precision? Recall?

### Part 4: Understand the model

1. Use the included `plot_roc` function to visualize the roc curve of each model. Note that you can pass parameters like this:

        plot_roc(X, y, RandomForestClassifier, n_estimators=20)

    Which model would you choose if I'm okay with a recall of 0.2?
    
1. Plot the feature importances as described in the lecture notes. Recall that `RandomForestClassifier` is a ensemble of many trees, and each individual tree will attribute different importances to different features. Extend the feature importance code to find the standard deviation of the importance for each feature across all trees. Add error bars to your chart, where the width of the bars is the equal to the standard deviation for that feature.
