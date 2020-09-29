import json
from pprint import pprint
from graph import Graph
import json

connections = [("A", "HHHH"), ("B", "C"), ("B", "D"),("C", "D"), ("E", "F"), ("F", "C")]
g = Graph(connections, directed=True)
g.add_Node("S")
g.add_Edge("A", "S")


print(g.print())
