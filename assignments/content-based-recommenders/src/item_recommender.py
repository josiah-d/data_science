from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np


class ItemRecommender():
    '''
    Content based item recommender
    '''
    def __init__(self, similarity_measure=None):
        pass

    def fit(self, X, titles):
        '''
        Takes a numpy array of the item attributes and creates the
        similarity matrix

        INPUT -
            X: NUMPY ARRAY - Rows are items, columns are feature values
            titles: LIST - List of the item names/titles in order of the
                            numpy arrray

        OUTPUT - None


        Notes:  You might want to keep titles and X as attributes
        to refer to them later

        Create the a similarity matrix of item to item similarity
        '''
        pass

    def get_recommendations(self, item, n=5):
        '''
        Returns the top n items related to the item passed in
        INPUT:
            item    - STRING - Name of item in the original DataFrame
            n       - INT    - Number of top related items to return
        OUTPUT:
            items - List of the top n related item names

        For a given item find the n most similar items to it (this can
        be done using the similarity matrix created in the fit method)
        '''
        pass

    def get_user_profile(self, items):
        '''
        Takes a list of items and returns a user profile. A vector
        representing the likes of the user.
        INPUT:
            items  -   LIST - list of movie names user likes / has seen

        OUTPUT:
            user_profile - NP ARRAY - array representing the likes of the user
                    The columns of this will match the columns of the trained
                    on matrix


        Using the list of items liked by the user create a profile which
        will be a 1 x number of features array.  This should be the
        addition of the values for all liked item features (you can
        choose how to normalize if you think it is needed)
        '''
        pass

    def get_user_recommendation(self, items, n=5):
        '''
        Takes a list of movies user liked and returns the top n items
        for that user

        INPUT
            items  -   LIST - list of movie names user likes / has seen
            n -  INT - number of items to return

        OUTPUT
            items - LIST - n recommended items


        Make use of the get_user_profile method to create a user profile
        that will be used to get the similarity to all items and
        recommend the top n.
        '''
        pass
