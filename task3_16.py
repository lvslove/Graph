from graph import Graph

g1=Graph()
g2=Graph()

g2.add_Node('7')
g2.add_Node('2')
g2.add_Edge('7','2')
g2.add_Node('1')
g1.add_Node('1')
g1.add_Node('2')
g1.add_Node('7')
g1.add_Edge('7','2')

g1.task3(g2)