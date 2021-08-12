import logging
import numpy as np
import pandas as pd

import pyspark as ps
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
import pyspark.sql.functions as F


class MovieRecommender_loop1():
    """Loop 1 recommender (see notebooks/solns.ipynb)
    Uses ALS out of the box"""
    def fit(self, training_df):
        self.als = ALS(rank=100,
              maxIter=10,
              regParam=0.1,
              userCol="user",
              itemCol="movie",
              ratingCol="rating")

        self.loop1_model = self.als.fit(training_df)

    def transform(self, requests_df):
        return(self.loop1_model.transform(requests_df))


class MovieRecommender_loop2():
    """Loop 2 recommender (see notebooks/solns.ipynb)
    Uses average per movie to fill up NaNs left by ALS"""
    def fit(self, training_df):
        self.avg_ratings = training_df.select('movie','rating')\
                                      .groupBy('movie')\
                                      .agg(F.avg('rating'))\
                                      .withColumnRenamed('avg(rating)','avg_rating')

    def transform(self, requests_df):
        return(requests_df.join(self.avg_ratings, 'movie', 'left')\
                          .withColumnRenamed('avg_rating','prediction'))


class MovieRecommender():
    """Aggregated results from loop1 and loop2 (by coaleste)"""
    def __init__(self):
        self.logger = logging.getLogger('reco-cs')
        self.spark = ps.sql.SparkSession.builder \
                    .master("local[4]") \
                    .appName("df lecture") \
                    .getOrCreate()
        self.sc = self.spark.sparkContext  # for the pre-2.0 sparkContext
        self.mr1 = MovieRecommender_loop1()
        self.mr2 = MovieRecommender_loop2()


    def fit(self, ratings):
        """
        Trains the recommender on a given set of ratings.

        Parameters
        ----------
        ratings : pandas dataframe, shape = (n_ratings, 4)
                  with columns 'user', 'movie', 'rating', 'timestamp'

        Returns
        -------
        self : object
            Returns self.
        """
        self.logger.debug("starting fit")

        self.training = self.spark.createDataFrame(ratings)

        self.training.persist()

        self.mr1.fit(self.training)
        self.mr2.fit(self.training)

        self.logger.debug("finishing fit")
        return(self)


    def transform(self, requests):
        """
        Predicts the ratings for a given set of requests.

        Parameters
        ----------
        requests : pandas dataframe, shape = (n_ratings, 2)
                  with columns 'user', 'movie'

        Returns
        -------
        dataframe : a *pandas* dataframe with columns 'user', 'movie', 'rating'
                    column 'rating' containing the predicted rating
        """
        self.logger.debug("starting predict")
        self.logger.debug("request count: {}".format(requests.shape[0]))

        self.requests = self.spark.createDataFrame(requests)

        pred_loop1 = self.mr1.transform(self.requests)\
                        .withColumnRenamed('prediction','prediction_loop1')

        pred_loop2 = self.mr2.transform(pred_loop1)\
                        .withColumnRenamed('prediction','prediction_loop2')

        results_loop2 = pred_loop2.withColumn('prediction',
                                      F.when(F.isnan('prediction_loop1'),
                                             F.col('prediction_loop2'))\
                                             .otherwise(F.col('prediction_loop1')))

        predictions = results_loop2.select('user', 'movie', 'prediction')\
                                   .withColumnRenamed('prediction','rating')\
                                   .toPandas()

        self.logger.debug("finishing predict")
        return(predictions)


if __name__ == "__main__":
    logger = logging.getLogger('reco-cs')
    logger.critical('you should use run.py instead')
