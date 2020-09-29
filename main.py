import json
from pprint import pprint
from graph import Graph
import json

connections = [("A", "HHHH"), ("B", "C"), ("B", "D"),
                   ("C", "D"), ("E", "F"), ("F", "C"), ("F", "HG")]
g = Graph(connections, directed=True)


print(json.dumps(g.to_dict(), ensure_ascii=False, indent=4))