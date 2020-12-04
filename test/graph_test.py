import unittest

from graph import Graph


class testGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_remove_node(self):
        self.assertEqual(self.graph.remove_Node('1'), None)
