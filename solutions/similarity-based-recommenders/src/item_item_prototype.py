import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity


def get_ratings_data():
    '''
    Returns:
        ratings_contents (dataframe): has columns "user", "movie", "rating"
        ratings_as_mat (sparse matrix): rows correspond to users and columns correspond
        to movies. Each element is the user's rating for that movie.
    '''
    ratings_contents = pd.read_table("data/u.data",
                                     names=["user", "movie", "rating",
                                            "timestamp"])
    ratings_as_mat = sparse.csr_matrix((ratings_contents.rating, 
        ((ratings_contents.user), (ratings_contents.movie))))
    return ratings_contents, ratings_as_mat


def load_movies():
    '''
    Return DF with movie Title and ID
    '''
    columns = """movie id | movie title | release date | video release date |          IMDb URL | unknown | Action | Adventure | Animation |
            Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western """
    columns = [word.strip() for word in columns.split('|')]
    columns = [word.replace(' ','_') for word in columns]
    movies = pd.read_table("./data/u.item", names= columns, sep='|', encoding='latin-1')
    movies = movies[['movie_id', 'movie_title']]
    return movies


def make_cos_sim_and_neighborhoods(ratings_mat, neighborhood_size):
    '''
    Args:
        ratings_mat (sparse matrix): 2-dimensional matrix of ratings
        neighborhood_size (int): number of similar items to look at 
    Returns:
        items_cos_sim (numpy array): an item-item matrix where each element is the
        cosine_similarity of the items at the corresponding row and column. This
        is a square matrix where the length of each dimension equals the number
        of columns in ratings_mat.

        neighborhood (numpy array): a 2-dimensional matrix where each row is the neighborhood
        for that item. The elements are the indices of the n (neighborhood_size)
        most similar items. Most similar items are at the end of the row.
    '''
    items_cos_sim = cosine_similarity(ratings_mat.T)
    least_to_most_sim_indexes = np.argsort(items_cos_sim, 1)
    neighborhood = least_to_most_sim_indexes[:, -neighborhood_size:]
    return items_cos_sim, neighborhood


def pred_one_user(items_cos_sim, neighborhoods, ratings_mat, user_id):
    '''
    Returns the predicted ratings for all items for a given user.
    '''
    n_items = ratings_mat.shape[1]
    items_rated_by_this_user = ratings_mat[user_id].nonzero()[1]
    # Just initializing so we have somewhere to put rating preds
    output = np.zeros(n_items)
    for item_to_rate in range(n_items):
        relevant_items = np.intersect1d(neighborhoods[item_to_rate],
                                        items_rated_by_this_user,
                                        assume_unique=True)
                                    # assume_unique speeds up intersection op
        # note: ratings_mat has data type `sparse_lil_matrix`, while
        # items_cos_sim is a numpy array. Luckily for us, multiplication
        # between these two classes is defined, and even more luckily,
        # it is defined to as the dot product. So the numerator
        # in the following expression is an array of a single float
        # (not an array of elementwise products as you would expect
        #  if both things were numpy arrays)
        output[item_to_rate] = (
            ratings_mat[user_id, relevant_items] * 
            items_cos_sim[item_to_rate, relevant_items] / 
            (items_cos_sim[item_to_rate, relevant_items].sum())
            )
    return output


if __name__ == '__main__':
    ratings_data_contents, ratings_mat = get_ratings_data()
    cos_sim, nbrhoods = make_cos_sim_and_neighborhoods(ratings_mat,
                                                       neighborhood_size=75)
    user_1_preds = pred_one_user(cos_sim, nbrhoods, ratings_mat, user_id=1)
    # Show predicted ratings for user #1
    print(user_1_preds)
