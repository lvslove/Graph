import collections
import json
from collections import defaultdict


class Graph(object):

    def __init__(self, directed=False):
        self._directed = directed
        self._graph = defaultdict(set)
        self.weight = defaultdict(set)
        # self.add_connections(connections)

    def add_Weight(self, node, x):
        self.weight[node].clear()
        if x == '':
            self.weight[node].add("default")
        else:
            self.weight[node].add(x)


    def nice_print(self):
        s, s2 = "\n", "\n"
        print("Graph")
        print(self.print_dir())
        for key in self._graph:
            s += '\t{"' + str(key) + '"}:' + str(self._graph[key]) + "\n"
        print(s)
        print("Weight")
        for key in self.weight:
            s2 += '\t{"' + str(key) + '"}:' + str(self.weight[key]) + "\n"
        print(s2)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add_Edge(node1, node2)

    def add_Edge(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def add_Node(self, node1):
        var = self._graph[node1]

    def remove_Edge(self, node1, node2):
        if not (self._graph.get(node1).isdisjoint({node2})):
            self._graph[node1].remove(node2)
            if not self._directed:
                self._graph[node2].remove(node1)
        else:
            print("Edge not exist")

    def remove_Node(self, node):
        for n, scans in self._graph.items():
            try:
                scans.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            print("Node", node, "not exist")
            pass

    # def is_connected(self, node1, node2):
    #     return node1 in self._graph and node2 in self._graph[node1]

    def write_in_file(self):
        self.update_file()
        s = ""
        for key in self._graph:
            s += '"' + str(key) + '":' + str(self._graph[key]) + ","
        nesting = s
        nesting = nesting.replace('}', ']')
        nesting = nesting.replace("'", '"')
        nesting = nesting.replace('{', '[')
        nesting = nesting.replace('set()', '{}')
        s = "{" + nesting + "}"
        nesting = s[:-2]
        nesting2 = nesting + "}"
        if self._directed:
            nestling3 = "yes"
        else:
            nestling3 = "no"
        z = str(self.weight)
        new = z[27:-2].replace("{", "").replace("}", "").replace("'", '"')
        res = "{" + new + "}"
        d = json.loads(nesting2)
        w = json.loads(res)
        file_path = 'json/output.json'
        with open(file_path) as f:
            data = json.load(f)
            data['datas'].append(d)
            data['directed'] = nestling3
            data['weight'].append(w)

            with open(file_path, 'w') as outfile:
                json.dump(data, outfile)

    @staticmethod
    def update_file():
        file_path = 'json/output.json'
        with open(file_path) as f:
            data = json.load(f)
            data['datas'] = []
            data['directed'] = []
            data['weight'] = []
            with open(file_path, 'w') as outfile:
                json.dump(data, outfile)

    def read_json(self):
        with open('json/input.json', 'r',
                  encoding='utf-8') as fh:  # открываем файл на чтение
            data = json.load(fh)
        if (data['directed']) == "yes":
            self._directed = True
        else:
            self._directed = False
        z = ""
        for value in data['datas']:
            for key in value:
                z += '"' + str(key) + '":' + str(value[key]) + ","
            nesting = z
            nesting = nesting.replace('}', ']')
            nesting = nesting.replace("'", '"')
            nesting = nesting.replace('{', '[')
            z = "{" + nesting + "}"
            nesting = z[:-2]
            nesting2 = nesting + "}"
            a = json.loads(nesting2)
        for n in a:
            self.add_Node(n)
            i = 0
            while len(a[n]) > i:
                self.add_Edge(n, a[n][i])
                i += 1
        z2 = "{"
        for value in data['weight']:
            for key in value:
                if value[key] != "":
                    z2 += '"' + str(key) + '":"' + str(value[key]) + '",'
                else:
                    z2 += '"' + str(key) + '":' + '"default"' + ","

        nesting = z2[:-1]
        nesting += '}'
        a = json.loads(nesting)
        for i in self._graph.keys():
            self.weight[i].add(a[i])

    def print_dir(self):
        if self._directed:
            return "Directed"
        else:
            return "Undirected"

    def task1_la(self):
        iz = []
        for key in self._graph:
            if (self._graph[key]) == set() or self._graph[key] == {key}:
                flag = True
                for key2 in self._graph:
                    if key in self._graph[key2] and key != key2:
                        flag = False
                if flag:
                    iz.append({key})
        print("Isolated nodes", iz)

    def task2_la(self):
        print("Write node")
        node = input()
        s = []
        z = []
        for i in self._graph.keys():
            for j in self._graph[i]:
                s.append((j, i))
        for i in range(0, len(s)):
            if s[i][0] == node:
                z.append(s[i][1])
            elif s[i][1] == node:
                z.append(s[i][0])
        print("All reachable node from", node, z)

    def task3(self, self2):
        if self2._graph.items() == self._graph.items():
            print(True)
            print("Graps match")
        else:
            print(False)
            print("Graps no match")

    def invert_list(self):
        g2 = Graph(True)
        for i in self._graph.keys():
            if self._graph[i] == set():
                g2.add_Node(i)
            else:
                for j in self._graph[i]:
                    g2.add_Edge(j, i)
        return g2

    def all_nodes(self):
        s = []
        for i in self._graph.keys():
            s.append(i)
            for j in self._graph[i]:
                s.append(j)
        duplicates = set(s)
        return duplicates

    def key_val(self):
        i = 0
        d = defaultdict(set)
        for j in self.all_nodes():
            d[i].add(j)
            i += 1
        return d

    def search_number(self, a):
        d = self.key_val()
        for i in d.keys():
            for j in d[i]:
                if j == a:
                    return i

    def set_num(self):
        nwe = defaultdict(set)
        for i in self._graph.keys():
            for j in self._graph[i]:
                nwe[self.search_number(i)].add(self.search_number(j))
        return nwe

    def list_sm(self):
        s = []
        adj = [[] for i in range(len(self.all_nodes()))]
        for i in self._graph.keys():
            for j in self._graph[i]:
                s.append((int(i), int(j)))
                adj[int(i) - 1].append(int(j) - 1)
        return adj

    def list_sm2(self):
        s = []
        adj = [[] for i in range(len(self.all_nodes()))]
        for i in self.set_num().keys():
            for j in self.set_num()[i]:
                adj[i].append(j)
                s.append((i, j))
        return adj

    def list_invert(self):
        s = list()
        adj = [[] for i in range(len(self.all_nodes()))]
        for i in self._graph.keys():
            for j in self._graph[i]:
                s.append((int(i), int(j)))
                adj[int(j) - 1].append(int(i) - 1)
        return adj

    def dfs(self, node, vis, order):
        vis[node] = True
        for i in self._graph[node]:
            if not (i in vis):
                self.dfs(i, vis, order)
        order.append(node)

    def dfsT(self, node, vis, comp):
        comp.append(node)
        vis[node] = True
        for i in self._graph[node]:
            if not (i in vis):
                self.dfsT(i, vis, comp)

    def bfs(self, node):
        visited, queue = set(), collections.deque([node])
        res = []
        visited.add(node)
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            for neighbour in self._graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                else:
                    return res
        return None

    def Task5(self):
        comp = []
        vis = dict()
        new = self.invert_list()
        order = []
        for i in self._graph.keys():
            if not (i in vis):
                self.dfs(i, vis, order)
        vis = dict()
        order.reverse()
        for i in order:
            if not (i in vis):
                new.dfsT(i, vis, comp)
                comp.append("n")
        return comp

    def comp_Task_5(self):
        s = defaultdict(set)
        z = 0
        for i in self.Task5():
            if i != "n":
                s[z].add(i)
            else:
                z += 1
        return s

    def print_comp_Task5(self):
        print("\nВывезти сильно связные компоненты графа")
        o = "\n"
        for key in self.comp_Task_5():
            o += "номер сильно связной компоненты " + str(key) + ": " + str(
                self.comp_Task_5()[key]) + "\n"
        print(o)
