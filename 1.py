from collections import defaultdict

from graph import Graph
g = Graph()
g2 = Graph(True)
g.read_json()
g.print_comp_Task5()
print("Введите вершину ")
z = input()
g.Task6(z)