class Vertex(object):
    """A Vertex class for use in graphs.

    Attributes
    ----------
    name: str
        The name of the Vertex.
    neighbors: dictionary
        neighbor(Vertex object): weight(float) key-value pairs.

    Methods
    -------
    add_neighbor
        Add a neighbor of the vertex to neighbors attribute.
    """

    def __init__(self, name):
        """Initialize a Vertex object."""
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        """Add a neighbor to the neighbors of the vertex.

        Parameters
        ----------
        neighbor: Vertex object
        weight: float

        Returns
        -------
        None
        """
        self.neighbors[neighbor] = weight


class Graph(object):
    """A Graph class to build graphs.

    Attributes
    ----------
    vertices: dictionary
        name(str): node(Vertex object) key-value pairs

    Methods
    -------
    add_node:
        Add a node to the graph.
    add_edge:
        Add input nodes to graph, add an edge between the two nodes.
    get_neighbors:
        Get the neighbors of the input node.
    """

    def __init__(self):
        """Initialize a Graph object."""
        self.vertices = {}

    def add_node(self, name):
        """Add a node to the graph.

        Parameters
        ----------
        name: str
            The name of the node to be added to the graph.

        Returns
        -------
        None
        """
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)

    def add_edge(self, a, b, weight):
        """Add input nodes to graph and add an edge between the two nodes.

        Parameters
        ----------
        a: str
            The name of node a.
        b: str
            The name of node b.
        weight: int or float
            The weight of the edge between node a and node b.
        """
        self.add_node(a)
        self.add_node(b)
        self.vertices[a].add_neighbor(b, weight)
        self.vertices[b].add_neighbor(a, weight)

    def get_neighbors(self, node):
        """Get the neighbors of the input node.

        node: str
            Name of the node to get the neighbors of.
        """
        if node in self.vertices:
            return self.vertices[node].neighbors
        return {}


def create_graph():
    """Create a weighted graph according to the given example in exercise.

    Parameters
    ----------
    None

    Returns
    -------
    g: Graph object
       Custom Graph object, not networkx.
    """
    g = Graph()
    g.add_edge('Sunset', 'Richmond', 4)
    g.add_edge('Presidio', 'Richmond', 1)
    g.add_edge('Pac Heights', 'Richmond', 8)
    g.add_edge('Western addition', 'Richmond', 7)
    g.add_edge('Western addition', 'Pac Heights', 2)
    g.add_edge('Western addition', 'Downtown', 3)
    g.add_edge('Western addition', 'Haight', 4)
    g.add_edge('Mission', 'Haight', 1)
    g.add_edge('Mission', 'Soma', 5)
    g.add_edge('Downtown', 'Soma', 5)
    g.add_edge('Downtown', 'Nob Hill', 2)
    g.add_edge('Marina', 'Pac Heights', 2)
    g.add_edge('Marina', 'Presidio', 4)
    g.add_edge('Marina', 'Russian Hill', 3)
    g.add_edge('Nob Hill', 'Russian Hill', 1)
    g.add_edge('North Beach', 'Russian Hill', 1)
    return g
