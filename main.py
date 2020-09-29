from graph import Graph
import json

defolt=[]
connections = [("A", "HHHH"), ("B", "C"), ("B", "D"),
                   ("C", "D"), ("E", "F"), ("F", "C"), ("F", "HG")]
g = Graph(connections, directed=True)

g.add_Edge('4','3')
new = Graph(defolt)

g.update_file()



