from graph import Graph
import pprint

connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
                   ('C', 'D'), ('E', 'F'), ('F', 'C')]
g = Graph(connections, directed=True)
pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(g._graph)