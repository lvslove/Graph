from collections import defaultdict

from graph import Graph

g = Graph()
g2 = Graph(True)
g.read_json()
adj = g.list_sm()  # список смежности орграфа
adjT = g.list_invert()  # список смежности транспонированного орграфа
count_nodes = len(g.all_nodes())
used = [False for i in range(count_nodes)]  # массив для хранения информации о пройденных и не пройденных вершинах
color = [int(0) for i in range(count_nodes)]  # массив для хранения цветов вершин
topSort = []  # топологически упорядоченная перестановка вершин графа
component = [int(0) for i in range(count_nodes)]  # массив для обозначения компонент сильной связности орграфа


def dfs(v):
    if used[v]:
        return
    used[v] = True
    for w in adj[v]:
        dfs(w)
        topSort.append(v)


def ccs(v, componentID):
    if used[v]:
        return
    used[v] = True  # помечаем вершину как пройденную
    component[v] = componentID
    # запускаем процедуру, которая топологически сортирует вершины графа
    for w in adjT[v]:
        ccs(w, componentID)


def run():
    for v in range(count_nodes):
        dfs(v)
    for i in range(count_nodes):
        used[i] = False
        componentID = 0
    for v in reversed(topSort):
        if not used[v]:
            ccs(v, componentID)
            componentID = componentID + 1
    print("\nКолличество компонент сильной связности =", componentID)  # выводим количество компонент сильной связности

    # for v in component:
    # print(v + 1, end=' ')
    # print(' ')


run()
s = []
for v in component:
    s.append(v + 1)
# print(s)
s1 = []
for i in range(1, count_nodes + 1):
    s1.append(i)
# print(s1)

i = 0
j = 1
final = defaultdict(set)
while i < count_nodes - 1:
    if s[i] == s[i + 1]:
        final[j].add(s1[i])
        final[j].add(s1[i + 1])
        i += 1
    elif s[i] != s[i + 1]:
        j += 1
        i += 1
print("\nКомпоненты связности")
print(final.items())

print("\n\ntask 6")
print("Введите вершину")
n = input()
for i in final.values():
    if int(n) in i:
        print(i)

