from collections import defaultdict


def load_imdb_data(filename):
    """Read in IMDB data from given filename and return two adjacency lists.

    One list for the actors and one list for the movies.

    Parameters
    ----------
    filename: str
        Name of imdb edge data file.

    Returns
    -------
    actors: defaultdict
        actor(str): movies(set) key-value pairs, adjacency list
    movies: defaultdict
        movie(str): actors(set) key-value pairs, adjacency list
    """
    with open(filename) as f:
        actors = defaultdict(set)
        movies = defaultdict(set)
        for line in f:
            actor, movie = line.strip().split('\t')
            actors[actor].add(movie)
            movies[movie].add(actor)
    return actors, movies
