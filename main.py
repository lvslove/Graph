from graph import Graph

defolt=[('1','4')]

g = Graph(defolt)
g.read_json()
g.nice_print()
g.remove_Node('d')
g.nice_print()
g.remove_Node('BLAT')
g.nice_print()
g.update_file()


