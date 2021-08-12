from collections import deque
from load_imdb_data import load_imdb_data
from sys import argv, exit


def shortest_path(actors, movies, actor1, actor2):
    """Return the shortest path from actor1 to actor2.

    If there is more than one path, return any of them.

    Parameters
    ----------
    actors: dictionary
        Adjacency list with actor(str): movies(set) key-value pairs.
    movies: dictionary
        Adjacency list with movie(str): actors(set) key-value pairs.
    actor1: str
        Actor to start at.
    actor2: str
        Actor to search for.

    Returns
    -------
    path: list
        List of actors and movies that starts at actor1 and ends at actor2
        or None if there is no such path.
    """
    pass


def print_path(path):
    """Print out the length of the path and all the nodes in the path.

    Parameters
    ----------
    path: list
        List of node names (strings)

    Returns
    -------
    None
    """
    if path:
        print("length:", (len(path) - 1) / 2)
        for i, item in enumerate(path):
            if i % 2 == 0:
                print("    {}".format(item))
            else:
                print(item)
    else:
        print("No path!")


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: python {} <data_file> <actor1> <actor2>".format(argv[0]))
        exit(1)
    filename = argv[1]
    actor1 = argv[2]
    actor2 = argv[3]
    actors, movies = load_imdb_data(filename)
    print("Searching for shortest path from {} to {}".format(actor1, actor2))
    path = shortest_path(actors, movies, actor1, actor2)
    print_path(path)
