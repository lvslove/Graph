import json
from collections import defaultdict



class Graph(object):

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def print(self, s=" "):
        for key in self._graph:
            s += (key,self._graph[key])
        return s




    def add_connections(self, connections):

        for node1, node2 in connections:
            self.add_Edge(node1, node2)

    def add_Edge(self, node1, node2):

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def add_Node(self, node1):
        self._graph[node1]


    def remove_Edge(self, node1, node2):


        self._graph[node1].remove(node2)
        if not self._directed:
            self._graph[node2].remove(node1)

    def remove_Node(self, node):


        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):


        return node1 in self._graph and node2 in self._graph[node1]


    def __write__(self):
        with open("data_file.json", "w") as write_file:
            json.dump(self.to_dict(), write_file)


