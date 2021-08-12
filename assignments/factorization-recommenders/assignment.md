# Matrix Factorization Based Recommenders

## Introduction
Now you'll use a matrix factorization 
approach for making recommendations. Since performance is important for recommendation
systems, we're going to use an existing library for computing our matrix
factorizations. This way, we can get started quickly, iterate quickly, and try lots of
things.

First, make sure you can run spark (either natively or in a docker container)

See [this file](https://github.com/GalvanizeDataScience/course-outline/blob/19-02-DS-SEA-g91/notes/docker_spark.md) for a review of using docker for a spark instance.

```python
import pyspark
```

## Basic
### Part 1: Creating a matrix factorization model

1. We will be using Apache Spark dataframes to store our data. In general,
a Spark dataframe is like a `pandas` DataFrame, but there are differences:
you can do similar things, but the syntax may be different.
The [API documentation](http://spark.apache.org/docs/latest/sql-programming-guide.html#datasets-and-dataframes)
includes examples in Scala, Java, Python, and R. When reading examples
in the Spark documentation, be sure to click on the Python tab: Scala
examples are shown by default, and they may be confusing to Python users.

You can convert between Spark dataframes and Pandas dataframes as needed, using the examples below.

```python
from pyspark.sql import SparkSession

# Setup a SparkSession
spark = SparkSession.builder.getOrCreate()
...

# Convert a Pandas DF to a Spark DF
spark_df = spark.createDataFrame(pandas_df) 

# Convert a Spark DF to a Pandas DF
pandas_df = spark_df.toPandas()
```

2. Use the ratings data located in `data/u.data` it is from the MovieLens data set.  Load the data into a spark dataframe. 

> HINT: `pd.read_csv` is very versatile; use the `delimiter` and `names` keyword arguments to load the `u.data` file. See `data/README` for details. Once the file is loaded into a pandas dataframe, `spark.createDataFrame` can convert it to a spark dataframe with an inferred schema.

3. We can discard the `timestamp` column since we won't be using it here.

4. Perform a train/test split on your Spark dataframe:

```python
train, test = ratings_df.randomSplit([0.8, 0.2], seed=427471138)
```

5. Get the density of your training data `num_rantings/ (num_users * num_movies)`


6. Create a matrix factorization model using the `pyspark.ml.recommendation.ALS` class ([documentation](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.recommendation.ALS.html), [examples](http://spark.apache.org/docs/latest/ml-collaborative-filtering.html)). Create an instance of this class. You should be able to train a minimal model by specifying just the `userCol`, `itemCol` and `ratingCol` arguments. We also want to be sure to use non-negative matrix factorization (NMF), which is not the default behavior.

```python
# Create an untrained ALS model.
from pyspark.ml.recommendation import ALS
als_model = ALS(
    itemCol='movie',
    userCol='user',
    ratingCol='rating',
    nonnegative=True,    
    regParam=0.1,
    rank=10) 
```

7. Call the `fit` method of your model. Note that Spark follows the *functional programming* paradigm, so Spark objects are *immutable*. In practice, this results in slightly different syntax:
 * **Scikit-Learn**: `als_model.fit(train)` in `sklearn` will cause `als_model` to be trained using the `train_X` dataset. In other words, the existing `als_model` will be trained in place. 
 * **Apache Spark**: `als_model.fit(train)` will *return* a trained version of `als_model`. Because `als_model` is a Spark object, it is *immutable* and remains unchanged.

```python
# Train the ALS model. We'll call the trained model `recommender`.
recommender = als_model.fit(train_df)
```

8. Call the `transform` method on your input data to get the predicted rating for user 1 of movie 100. 

Note 1: You can use the following snippet of code to create a Spark dataframe with just the single datapoint:

```python
one_row_pandas_df = pd.DataFrame({'user': [1], 'movie': [100]})
one_row_spark_df = spark.createDataFrame(one_row_pandas_df)
```

Note 2: Spark dataframes have a different interface than Pandas dataframes. Here's a quick example of how to show their contents. Of course, you can refer to the Spark documentation for more examples.

```
>>> one_row_spark_df
DataFrame[movie: bigint, user: bigint]

>>> one_row_spark_df.show()
+-----+----+
|movie|user|
+-----+----+
|  100|   1|
+-----+----+
```

9. Inspect the `recommender.itemFactors` and `recommender.userFactors` dataframes to see the latent factors that your model has extracted from the data. What are the dimensions of the matrices that these two dataframes represent?

10. Without using the `transform` method, compute the predicted rating for user 1 of movie 100.

Hint: Start by getting the user factors for user 1, and the item factors for movie 100.

11. Call the `transform` method on your training data to get a dataframe of the predicted ratings. Remember that Spark dataframes are *immutable*, so the result will be returned as a new dataframe that includes a `predictions` column.

12. Does the transformed training data include any missing values?  Did you expect it to?  Does it include predicted ratings for all user, movie combinations?

13. Take a look at your predictions using the new dataframe's `.show()` method and examine their descriptive statistics with `.describe()`. Does anything stand out as a potential issue?

14. Look into the [recommendForUserSubset](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.recommendation.ALSModel.html?highlight=recommendforusersubset#pyspark.ml.recommendation.ALSModel.recommendForUserSubset) documentation and use it to get the top 10 recommendations for user 1.

### Part 2: Implicit recommendations

Implicit recommendations have a slightly different method to they way they are computed.  The basic for the use is that a `1` represents having seen it and `0` not.  It can be used in a more complex manor however by including the amount of times the user interacted with the item. Think of a music streaming service if you have listened to a song 10 times it can be inferred you like the song more then one listened to once. Percentages of movie watched can be used as well. 

1. Modify the `train` dataset so that there is a new column of `1` to represent the movie having been seen.  Using an implicit implementation of ALS train the model on the data using the new field as the `ratingCol`. Look at the documentation to do this [here](https://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.recommendation.ALS).  


2. Look at the top 10 recommended movies for user 1 again. Before doing so do you expect the movies to be the same or not?

3. It is common to use other values then just `1` and `0` in implicit rating.  What other values could you use?  What if you where YouTube?  What about Spotify? 

4. Train another implicit ALS model.  This time use the `rating` column with the explicit values.  You are going to treat those as number of times the movie was viewed by the user. Get the 10 most recommended movies for user 1 again and compare the results.

## Advanced
### Part 3: Evaluation


**REMINDER: You can cast a Spark dataframe to a Pandas dataframe using its `.toPandas()` method.**

1. Use the explicit ALS model to transform the test dataset.  Fill in any missing values with the average rating found in the training dataset. (Extra credit: can you think of a better value to use in the event of "cold start" issues?)

2. Calculate the RMSE of your predictions on the training and testing data.

3. Overall RMSE doesn't tell the whole story of how your model is performing. For example, is your model better at predicting high ratings than low ratings? Find out by answering the following questions:
- What is the RMSE just for the data whose true rating is `1`? (compare train RMSE & test RMSE).
- What about for data where the true rating is `2`? `3`? `4`? `5`?
- Make a histogram of your predicted ratings just for data with true rating `1` (then repeat for `2` through `5`). What patterns do you see?
- You can put all these histograms in a single violin plot, with the true ratings on the horizontal axis and histograms (or KDEs of the histograms) plotted vertically. Use the following snippet (adapted from [this matplotlib example](http://matplotlib.org/examples/statistics/violinplot_demo.html)) to make such a plot for both the training and the testing data.
```python
## you have to create the subsets.
## preds_for_actual_1s should contain all the predicted
## ratings for data with actual rating 1. etc.
data_subsets = [preds_for_actual_1s, preds_for_actual_2s, preds_for_actual_3s, ...]
positions = [1,2,3,4,5]

plt.violinplot(data_subsets, positions)
```
(see the violinplot [documentation](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.violinplot.html))

4. Regularization. What if the cost function changed from <br>
![ALS Objective](images/als_objective.png) <br>
to <br>
![Regularized Objective](images/reg_als_objective.png) <br>
Using what you know about regularization from linear regression, what effect would you expect this to have on solutions? What would you expect to see in the difference of training RMSE between setting this parameter to 0 or 1e-4? Try it.

#### What are the latent features?

5. Can you construct an intuitive explanation for what the latent features represent? What are the top movies represented by each latent feature? Try comparing the correlation of the latent feature with the movie ratings (perhaps using scipy's cdist) then match the movie ids to titles and see what you can find. How might you use this information? Remember, the _user_ coefficients are the ones that describe a user's affinity for a type of movie, so you'll want to use those (conversely the movie features describe the kinds of users to which that movie appeals)!

6. Similarly, what are the top genres represented by each latent feature?

#### Parameter Tuning

With tuning parameters how should we know what the best value for those parameters is? Easy, our old friend Cross-Validation. Spark has a [CrossValidator](https://spark.apache.org/docs/latest/ml-tuning.html) class that you can use along with `ParamGridBuilder` and `RegressionEvaluator` to define and search a parameter grid for the best parameters.

7. Tune your model to find the best parameters for `rank` and `regParam`. What parameters did you find?


## Extra Credit
### Part 4: More evaluation

1) Evaluation of recommenders is difficult.  While A/B testing is the best way to validate a recommender other methods of validation are needed.  One example from the paper [Collaborative Filtering for Implicit Feedback Datasets](http://yifanhu.net/PUB/cf.pdf).  It is a rank method.  It is used to score Implicit recommenders where the number of interactions with a item is recorded.  The formula is:
$$
\overline{rank} = \frac{\sum_{u,i} r^t_{ui} * rank_{ui}}{\sum_{u,i} r^t_{ui}}
$$
Where:
$r^t_{ui}$ is the # of interactions for observations in the test set.
$rank_{ui}$ are the percentile ranking of each item for each user.

Work through the math first.  How does getting the order of recommendations wrong affect the math?

2) Implement a function that will take a dataframe with columns of `user`, `movie`, `interactions`, `prediction` and calculates the rank.
