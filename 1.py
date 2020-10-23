from collections import defaultdict

from graph import Graph
g = Graph()
g.read_json()
g.nice_print()
d = defaultdict(set)
#print(g.all_nodes())
#print(g.key_val())

print(g.list_sm())
print(g.list_sm2())
