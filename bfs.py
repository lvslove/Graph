from collections import defaultdict
from graph import Graph

g = Graph()
g.read_json()
x = str(input())
print(g.bfs(x))
