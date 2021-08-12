# Item-based collaborative filtering
# Building an Item-Based collaborative filtering engine

## Introduction

You have received a small prototype for an item-item based recommender, and your job is to turn it into a python class that can be used as the basis for a recommendation engine on a small website.

You will be using the [MovieLens](http://grouplens.org/datasets/movielens/) dataset for this sprint. This data contains movie ratings on a scale from 1-5 in the [u.data](data/u.data) file.  There are other files we won't be using at this time, and they are described in the [readme](data/README).

You can also use this small toy dataset for verifying that your code is running properly.

```python
ratings_mat = sparse.lil_matrix(np.array([[4, 0, 0, 5, 1, 0, 0],
                                          [5, 5, 4, 0, 0, 0, 0],
                                          [0, 0, 0, 2, 4, 5, 0],
                                          [0, 3, 0, 0, 0, 0, 3]]))
```

## Basic

### Part 1: The data
One of the biggest problems with collaborative recommenders is the recommendations are based on the amount of ratings in the data.  This leads to the cold start problem and issues with how good a recommendation is depending on the amount of data one has for a individual or item.  Before going forward we need to look at the data

1. Load the data from `data/u.data`.  This can be done with the command `ratings_contents = pd.read_table("./data/u.data", names=["user", "movie", "rating", "timestamp"])`.  

2. Get the count of how many ratings each user and each movie have in this dataset.  Plot a histogram of each and get the minimum and maximum for each. This is a first step you should always take.  What do you see?

3. What is the density of our data `rated_items / (num_items * num_users)`? Density is the percent of a utility matrix which is populated. rated_items will be the number of data points, or populated cells. After transformation into a utility matrix, the num_items == num_unique_items, and num_users == num_unique_users. Remember, "items" are movies in our example.

4. Will we have to worry about the cold start problem?  What about when splitting for testing?  Take a sample of the data and check the counts again.

5. What method could we employ for recommendations if we run into the cold start problem?  

6. Implement a simple popularity method by item for recommendation.  What is the top movie?

7. (Extra credit get back to if time) Implement a dampened mean popularity method.  $$\frac{\sum_{i} r_{ui} + (k * u)}{ n_i + k }$$

Where:
$u$ is global mean
$k$ is a control factor (ie 5)
$n_i$ is the number of ratings for product i
$r_ui$ is the rating for item $i$ by user $u$   

8. When might these methods be useful?  

### Part 2: An item-item recommender
1. Review `item_item_prototype.py` and then run it. There are a few serious problems with the ratings shown.

	Come up with a hypothesis for why we are getting `nan`'s in our predictions. Write your explanation for why we are getting `nan`'s in a file called `explanations.txt`.

2.  Move all of our functionality from the prototype to a class called `ItemItemRecommender`. `src/ItemItemRecommender.py` has a basic skeleton for a class.  The skeleton follows the convention of sklearn, where the `__init__` function describes the parameters of the model (in this case, it takes the neighborhood size as an argument and sets `self.neighborhood_size`).  Then a `fit` method of the class takes the data (in this case `ratings_mat`) and sets everything else in the `make_cos_sim_and_neighborhoods` function.

	Do not call the `fit` method from the constructor.  To match the common convention, let the user of the class do that.

	Add code outside the class so you can run this file and get the same output you got in the prototype.

3.  Modify `pred_one_user` to replace the missing values with something numerical. `numpy.nan_to_num` is a good option for this.

4.  Add a `pred_all_users` method. The output should be a 2-dimensional array with the same shape as the matrix of actual ratings. Accomplish this by calling your `pred_one_user` method repeatedly.

5.  In a live setting, we'd have to be able to make recommendations for a single user quickly. Add an optional argument to pred_one_user that indicates whether to print the running time.  This argument should default to False.  Add `from time import time` to the imports part of this file. Add the functionality in `pred_one_user` to print running time when requested. Which configurations of your recommender result in shorter times? What things could you compute in advance to make your recommender more performant? What are the downsides of this pre-computing?

6.  Add a method to return the indices (column numbers) of the top n recommendations for a user.  Exclude items the user has already rated. This method should take the user_id and n as arguments.  It should return a list. Use `np.argsort`. Then be careful to preserve that ordering when you remove the already-rated items.

7.  What do you think are the major shortcomings of the current recommender?  Write your answer in `explanations.txt`. If you have any ideas, suggest possible remedies.

## Advanced
### Part 3: Evaluation 

Evaluation of a recommender system is something that will be revisited several times. 

1. What is the draw back to just RMSE on a test set?  Put your answer into `explanations.txt`.

2. What is another method that can be used that may work better?

3. Get predictions for several users who show up in your test set and compare the predictions with the actual values in the test set.  

4. Write a function that will get the RMSE for a given user do the amount of ratings for by the user make better recommendations?


## Extra Credit
### Part 4: Content-based recommenders

Looking back on what you did this morning how could you use user ratings with content based recommendations? 
