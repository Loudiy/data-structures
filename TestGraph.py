import unittest
from graph import Vertex, Edge, GraphAdjList

class TestVertex(unittest.TestCase):

    def test_initialization(self):
        key = 15
        value = 20
        vertex = Vertex(key, value)
        self.assertIsInstance(vertex, Vertex)
        self.assertEqual(vertex.key, key)
        self.assertEqual(vertex.value, value)

    def test_equality(self):
        key = 15
        value = 20
        u = Vertex(key, value)
        v = Vertex(key, value)

        self.assertTrue(u == v)
        self.assertEqual(u, v)

    def test_hash(self):
        key = 15
        value = 20
        u = Vertex(key, value)
        v = Vertex(key, value)

        self.assertEqual(hash(u), hash(v))

class TestEdge(unittest.TestCase):

    def test_initialization(self):
        u = Vertex(15, 20)
        v = Vertex(1, 2)
        w = 10
        edge = Edge(u, v, w)
        self.assertIsInstance(edge, Edge)
        self.assertIs(edge.u, u)
        self.assertIs(edge.v, v)
        self.assertEqual(edge.weight, w)


class TestGraphAdjList(unittest.TestCase):

    def test_initialization(self):
        u = Vertex(15, 20)
        uu = Vertex(15, 20)
        v = Vertex(1, 2)
        w = 10
        edge = Edge(u, v, w)
        graph = GraphAdjList()
        self.assertIsInstance(graph, GraphAdjList)
        graph.add_vertex(u)
        graph.add_vertex(v)
        self.assertEqual({u, v}, graph.vertices)
        self.assertEqual({u: dict(), v: dict()}, graph.adj)
        graph.add_edge(edge)
        self.assertEqual({u: {v: w}, v: dict()}, graph.adj)
        self.assertEqual({v:w}, graph.adj[uu])

    def test_bfs(self):
        graph = GraphAdjList()
        graph.add_edge(Edge(Vertex('s', 0), Vertex('a', 1)))
        graph.add_edge(Edge(Vertex('s', 0), Vertex('c', 1)))
        graph.add_edge(Edge(Vertex('d', 2), Vertex('b', 3)))
        graph.add_edge(Edge(Vertex('a', 1), Vertex('d', 2)))
        graph.add_edge(Edge(Vertex('c', 1), Vertex('d', 2)))
        graph.add_edge(Edge(Vertex('b', 3), Vertex('a', 1)))
        graph.add_edge(Edge(Vertex('c', 1), Vertex('f', 2)))
        graph.add_edge(Edge(Vertex('f', 2), Vertex('e', 3)))
        graph.add_edge(Edge(Vertex('e', 3), Vertex('c', 1)))
        graph.add_edge(Edge(Vertex('f', 2), Vertex('h', 3)))
        graph.add_edge(Edge(Vertex('h', 3), Vertex('g', 3)))
        graph.add_edge(Edge(Vertex('g', 3), Vertex('f', 2)))
        graph.add_edge(Edge(Vertex('f', 2), Vertex('g', 3)))
        graph.bfs(Vertex('s', 0))
        for vertex in graph.vertices:
            self.assertEqual(vertex.d, vertex.value)

    def test_dfs(self):
        graph = GraphAdjList()
        a = Vertex('a', (2, 7))
        b = Vertex('b', (1, 12))
        c = Vertex('c', (8, 11))
        d = Vertex('d', (9, 10))
        e = Vertex('e', (13, 16))
        f = Vertex('f', (14, 15))
        g = Vertex('g', (5, 6))
        h = Vertex('h', (3, 4))
        graph.add_edge(Edge(b, a))
        graph.add_edge(Edge(h, b))
        graph.add_edge(Edge(a, h))
        graph.add_edge(Edge(a, g))
        graph.add_edge(Edge(g, h))
        graph.add_edge(Edge(b, g))
        graph.add_edge(Edge(b, c))
        graph.add_edge(Edge(c, g))
        graph.add_edge(Edge(c, d))
        graph.add_edge(Edge(d, g))
        graph.add_edge(Edge(e, c))
        graph.add_edge(Edge(e, d))
        graph.add_edge(Edge(e, f))
        graph.add_edge(Edge(f, g))
        graph.dfs()
        for vertex in graph.vertices:
            self.assertEqual(vertex.color, "Black")


if __name__ == '__main__':
    unittest.main()