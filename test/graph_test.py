import unittest

from graph import Graph


class testGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
    def test_add_node(self):
        self.assertEqual(self.graph.add_Node('1'),self.graph.check())

    def test_remove_node(self):
        self.assertEqual(self.graph.remove_Node('1'),None)
