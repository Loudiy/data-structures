"""This file contains representation of different graphs as well as
all the elements necessary for those graph.

This file is created by Nessreddine LOUDIY."""


class Vertex:
    """A class to represent a Vertex."""

    """Vertex initialization."""
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    """Implement == operation."""
    def __eq__(self, other):
        return self.key == other.key \
               and self.value == other.value \
               and self.__class__ == other.__class__

    """Implement the hash function of the Vertex.
    Otherwise the Vertex object can't be added to any dictionary/set!
    In fact, python3 makes an object unhashable when implementing __eq__ without __hash__.
    The following link explains the reason behind implementing this method:
    https://docs.python.org/3/glossary.html#term-hashable
    Some other good resources that explain why you should implement a __hash__ method when you implement __eq__ if 
    you would like to use those objects in sets and dictionaries:
    https://hynek.me/articles/hashes-and-equality/
    http://zetcode.com/python/hashing/"""
    def __hash__(self):
        return hash((self.__class__, self.key, self.value))


class Edge:
    """A class to represent an Edge."""

    """Edge initialization."""
    def __init__(self, u: Vertex, v: Vertex, w=None):
        self.u = u
        self.v = v
        self.weight = w


class GraphAdjList:
    """Class to represents a Directed Graph using Adjacency Lists."""

    """GraphAdjList initialization."""
    def __init__(self):
        self.adj = dict()
        self.vertices = set()

    """Function to add a vertex to the graph."""
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        self.adj[vertex] = dict()

    """Function to add an edge to the graph."""
    def add_edge(self, edge):
        if edge.u not in self.vertices:
            self.add_vertex(edge.u)
        if edge.v not in self.vertices:
            self.add_vertex(edge.v)

        for vertex in self.vertices:
            if vertex == edge.u:
                u = vertex
            if vertex == edge.v:
                v = vertex
        self.adj[u][v] = edge.weight

    """Function to perform a Breath-First Search."""
    def bfs(self, s):
        for vertex in self.vertices:
            if vertex == s:
                source = vertex
            vertex.d = float('Inf') if vertex != s else 0
        queue = [source]
        while queue:
            u = queue.pop()
            for vertex in self.adj[u]:
                if vertex.d == float('Inf'):
                    vertex.d = u.d + 1
                    queue.append(vertex)

    """Function to perform a Depth-First Search."""
    def dfs(self):
        for vertex in self.vertices:
            vertex.color = "White"
        time = 0
        for vertex in self.vertices:
            if vertex.color == "White":
                time = self.dfs_visit(vertex, time)

    """Auxiliary function for DFS"""
    def dfs_visit(self, vertex, time):
        time = time + 1
        vertex.d = time
        vertex.color = "Gray"
        for v in self.adj[vertex]:
            if v.color == "White":
                time = self.dfs_visit(v, time)
        vertex.color = "Black"
        time = time + 1
        vertex.f = time
        return time
