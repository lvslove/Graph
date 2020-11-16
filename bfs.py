from collections import defaultdict
from graph import Graph

g = Graph()
g.read_json()
g.nice_print()



g2 = Graph(True)

g2.add_Edge("0", "3")
g2.add_Edge("4","0")
g2.nice_print()


for i in g._graph.keys():
    for j in g2._graph.keys():
        if i == j:
            print(i, ":", g._graph[i].intersection(g2._graph[j]))

#идем по значениям и елси равны сравниваем через объединение значения, это для того чтобы типо если вхождили не все знаяения
#пример аыше показательный
#отсавлю код и вынесу в фунцию

print("\nвывод говна через функцию")
g.NIK_task3_xz(g2)









