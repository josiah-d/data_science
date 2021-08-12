from collections import deque
from src.load_imdb_data import load_imdb_data
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
    graph = actors.copy()
    graph.update(movies)

    queue = deque([actor1])
    path = {actor1: [actor1]}

    while len(queue) > 0:
        node = queue.popleft()   # popleft gives us the FIFO ordering we want from our queue
        if node == actor2:
            return path[node]
        for neighbor in graph[node]:
            if neighbor in path:
                continue   # <-- skipping this neighbor because we already
                           #     have the shortest path for it
            path_to_neighbor = path[node] + [neighbor]
            path[neighbor] = path_to_neighbor
            queue.append(neighbor)

    return None   # <-- indicates no path found


def shortest_paths(actors, movies, actor1, actor2):
    """Return the shortest paths from actor1 to actor2.

    If there is more than one path, return ALL of them.

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
    paths: list
        List of paths, where each path is a list of actors and movies
        that starts at actor1 and ends at actor2.
    """
    graph = actors.copy()
    graph.update(movies)

    queue = deque([actor1])
    path = {actor1: [[actor1]]}   # <-- notice the list of lists!

    while len(queue) > 0:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor in path:
                # Hum... we found a neighbor that we already have a
                # shortest path recorded for. If this new path we've
                # just found is equally short, we need to record it too.
                # But if it's longer, we can skip this neighbor since we
                # already have a shortest path for it.
                length = len(path[neighbor][0])
                if length < len(path[node][0]) + 1:
                    continue
            else:
                path[neighbor] = []
                queue.append(neighbor)

            for path_to_me in path[node]:
                # This is vital: We can get to our neighbor from ANY path
                # which goes to us. So, we'll record all these options as
                # ways to get to our neighbor.
                path_to_neighbor = path_to_me + [neighbor]
                path[neighbor].append(path_to_neighbor)

    # Notice we're checking this condition at the bottom here, since we
    # never know if we've finished searching for alternative paths until
    # we've searched the whole graph.
    if actor2 in path:
        return path[actor2]
    return None


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
        print("length:", (len(path) -1) / 2)
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

    #path = shortest_path(actors, movies, actor1, actor2)
    #print_path(path)

    paths = shortest_paths(actors, movies, actor1, actor2)
    for path in paths:
        print_path(path)
        print()
    print('Found {} paths.'.format(len(paths)))
