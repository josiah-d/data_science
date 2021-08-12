# Decision Trees
- [Decision Trees](#decision-trees)
  - [Introduction](#introduction)
    - [Play Golf Dataset](#play-golf-dataset)
    - [Pseudo-code](#pseudo-code)
  - [Basic](#basic)
    - [Part 1: Implementation](#part-1-implementation)
      - [Steps to Implementing](#steps-to-implementing)
  - [Advanced](#advanced)
    - [Part 2: Decision Trees for Regression](#part-2-decision-trees-for-regression)
  - [Extra Credit](#extra-credit)
    - [Part 3: Pruning](#part-3-pruning)
    - [Part 4: A Real Dataset](#part-4-a-real-dataset)
## Introduction

### Play Golf Dataset

When implementing any ML algorithm for the first time, it is often easier to start with a trivially simple data set. You should always focus on one portion of the pipeline at a time: we do not want worry about cleaning data during feature selection just as we do not want to worry about feature engineering when writing our model building code.  We will be using the canonical 'Play Golf' [dataset](http://www2.cs.uregina.ca/~dbd/cs831/notes/ml/dtrees/c4.5/c4.5_prob1.html) when writing our algorithm.

Look at the [golf data](data/playgolf.csv). You will also see a dataset with just the categorical features and one with just the continuous features. Starting with just categorical features may be easier for implementation.

### Pseudo-code

Here's the pseudocode for the algorithm you will be implementing.

    function BuildTree:
        If every item in the dataset is in the same class
        or there is no feature left to split the data:
            return a leaf node with the class label
        Else:
            find the best feature and value to split the data
            split the dataset
            create a node
            for each split
                call BuildTree and add the result as a child of the node
            return node

## Basic

### Part 1: Implementation
You've been given starter code in the [src](src) folder. Some of the instance variables chosen are not the only possible way of implementing a decision tree, so feel free to modify anything if it fits your implementation better.

* The `TreeNode` class is implemented. These are the instance variables:

    * `column` (int): index of feature to split on
    * `split_value` (object): value of the feature to split on
    * `categorical` (bool): whether or not node is split on a categorial feature (vs continuous)
    * `name` (string): name of the feature (or name of the class in the case of a list)
    * `left` (TreeNode): left child
    * `right` (Tree Node): right child
    * `leaf` (boolean): true or false depending on if the node is a leaf node.
    * `classes` (Counter): if a leaf, a count of all the list of all the classes of the data points that terminate at this leaf.  Can be used to assess how "accurate" an individual leaf is.

    The `as_string` and `__str__` functions are designed to print out the decision tree (mostly for debugging).

* There is starter code for the `DecisionTree` class. You will need to fill in the class so that you can use your decision tree code as follows (also see `src/run_decision_tree.py`).

    ```python
    tree = DecisionTree()
    tree.fit(X, y, df.columns[:-1])
    print(tree)
    y_predict = tree.predict(X)
    ```

    You can see that the `__str__` method is implemented for you. This enables you to print your tree for debugging purposes.

* The `__init__`, `fit`, `_build_tree` and `__str__` methods are already implemented for you. You will need to implement the other ones.

* There are minimal tests in `src/test_decision_tree.py`. One test for each method you need to implement. You can run the tests with this command:

    ```
    pytest src/test_decision_tree.py
    ```

* The file `run_decision_tree.py` should run your Decision Tree code, print the resulting decision tree and show the predicted results.

#### Steps to Implementing

We will be implementing the **CART** algorithm. This means that every split will be binary. For categorical features, splits will be like: `sunny` or `not sunny`. For continuous features, splits will be like: `<80` or `>=80`.

1. Implement the `_entropy` method, which is given by the following equation. Entropy measures the amount of "disorder" in a set. Here there are *m* classes in the set and *ci* is the *i*-th class of our target y.

    ![shannon entropy](images/entropy.png)

    *P(c)* = (count of occurrences of class *c*) / size of *y*

    Note that to calculate entropy, you only need the labels (`y` values) and none of the feature values.

2. Implement the `_gini` method. Your information gain method will be able to use either gini or entropy.

    ![gini impurity](images/gini.png)

3. Implement the `_make_split` method. This should take the index of the feature and the value of the feature and make the split of the data into two subsets. Note that for categorical features this should split on whether it's equal to the value or not. For continuous, it should split on `<` or `>=`.

4. Implement the `_information_gain` method. This should take a split (the result of the `_make_split` method) and return the value of the information gain.

5. Implement the `_choose_split_index` method. This should take the data and try every possible feature and value to split on. It should find the one with the best information gain.

6. The `predict` method in the Decision Tree class is implemented by calling the `predict_one` method in the `TreeNode` class. You need to finish the implementation of the `predict_one` method by giving the conditions for when you should move left or right on the decision tree.

## Advanced

### Part 2: Decision Trees for Regression
**Note:** Before starting this, make sure you commit your code with a `git commit`! Don't lose your past results with your new changes!

You can use decision trees for predicting continuous values as well. Instead of using entropy to calculate the disorder in the set, we use the variance.

To get to value of a leaf node, average all of the values.

1. Make your decision tree able to predict continuous values. You can modify your decision tree class so that it can do either continuous or categorical depending on what parameters you pass it, or just copy and create a new class. For checking out if your code is implemented correctly, you can use the same dataset and predict one of the continuous variables.

2. Implement model trees, which are predictors which start by using a decision tree, but use linear regression to predict the value on each leaf node. Details can be found in 9.5 of Machine Learning in Action.

## Extra Credit

### Part 3: Pruning
*Pruning* is designed to simplify the tree so it doesn't go so deep. It is a way of stopping earlier or merging leaves that helps deal with overfitting. The first two extra credit problems are implementing prepruning and postpruning. A well designed decision tree would have these implemented.

1. *Prepruning* is making the decision tree algorithm stop early. Here are a few ways that we preprune:
    * leaf size: Stop when the number of data points for a leaf gets below a threshold
    * depth: Stop when the depth of the tree (distance from root to leaf) reaches a threshold
    * mostly the same: Stop when some percent of the data points are the same (rather than all the same)
    * error threshold: Stop when the error reduction (information gain) isn't improved significantly.

    Implement some of the prepruning thresholds and play around with using them.

2. Implement *postpruning* for your decision tree. You build the tree the same as before, but after you've built the tree, merge some nodes together if doing so reduces the test-set error. Here's the psuedocode:

        function Prune:
            if either left or right is not a leaf:
                call Prune on that split
            if both left and right are leaf nodes:
                calculate error associated with merging two nodes
                calculate error associated without merging two nodes
                if merging results in lower error:
                    merge the leaf nodes

    You can find more detail in section 9.4.2 in Machine Learning in Action.


### Part 4: A Real Dataset

1. Try running your decision tree code on a previous exercise's dataset.

2. Use sklearn's [Decision Tree](http://scikit-learn.org/stable/modules/tree.html#classification). How well does it do compared to logistic regression?
 
3. Implement "model trees", which are predictors which start by using a decision tree, but use linear regression to predict the value on each leaf node. Details can be found in 9.5 of Machine Learning in Action.
