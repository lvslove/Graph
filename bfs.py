from collections import defaultdict

from graph import Graph

g = Graph()
g.read_json()
govno = defaultdict(set)
lenght = len(g.all_nodes())

#print(g.bfs("1"))

s = []
for i in g._graph.keys():
    print(g.bfs(i))

