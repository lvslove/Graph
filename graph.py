import json
from collections import defaultdict
from pprint import pprint

from collection_json import Collection


class Graph(object):

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def to_dict(self):
        fields = {
            'направленный': self._directed,
            'items': Collection.__format__(self._graph),
        }
        return fields

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



    def __str__(self):
        return '"[{},{}]"'.format(self._directed, dict(self._graph))

    def __write__(self):
        s = json.loads(self.__str__())
        with open("data_file.json", "w") as write_file:
            json.dump(s, write_file)


