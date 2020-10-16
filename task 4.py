from graph import Graph


g = Graph()
g2 = Graph(True)
g.read_json()
g.nice_print()
g2 = g.invert_list(g2)
g2.nice_print()
print(g.DFS("1"))
