
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

class ItemItemRecommender(object):
    """Item-item similarity recommender."""

    def __init__(self):
        """Initialize the parameters of the model."""
        pass

    def fit(self):
        """Fit the model to the data specified as an argument.
        Store objects for describing model fit as class attributes.
        """
        pass

    def _set_neighborhoods(self):
        """Get the items most similar to each other item.
        Should set a class attribute with a matrix with number of rows
        equal to number of items, and number of columns equal to
        neighborhood size. Entries in this matrix will be indices of other
        items.
        You will call this in your fit method.
        """
        pass

    def pred_one_user(self):
        """Accept user id as arg. Return the predictions for a single user.
        Optional argument to specify whether or not timing should be
        provided on this operation.
        """
        pass

    def pred_all_users(self):
        """Return a matrix of predictions for all users.
        Repeated calls of pred_one_user, are combined into a single matrix.
        Return value is matrix of users (rows) items (columns) and
        predicted ratings (values).
        Optional argument to specify whether or not timing should be
        provided on this operation.
        """
        pass

    def top_n_recs(self):
        """Take user_id argument and number argument.
        Return that number of items with the highest predicted ratings,
        after removing items that user has already rated.
        """
        pass
