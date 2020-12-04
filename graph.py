import collections
from pprint import pprint

import json
from collections import defaultdict


class Graph(object):

    def __init__(self, directed=False):
        self._directed = directed
        self._graph = defaultdict(set)
        self.weight = defaultdict(set)
        self.graph = []  # default dictionary
        # self.add_connections(connections)

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
            del self.weight[node]
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

    def dfs_c(self, visited, node, list1):
        if node not in visited:
            list1.append(node)
            visited.add(node)
            for neighbour in self._graph[node]:
                self.dfs_c(visited, neighbour, list1)
        return list1

    def check_connected(self):
        list1 = []
        keys = list(self._graph.keys())
        visited = set()
        if len(self.dfs_c(visited, keys[0], list1)) == self.len_node():
            return True
        else:
            return False

    def number_node(self):
        num = []
        j = 0
        a = list(self.all_nodes())
        while a:
            num.append([a.pop(), j])
            j += 1
        print(num)

    def list_m(self):
        s = []
        for i in list(self._graph.keys()):
            a = list(self._graph[i])
            while a:
                s.append([i, a.pop()])
        return s

    # [номер, смежная вершина, вес]

    def list_num(self):
        s = []
        a = (self.list_m())
        while a:
            s.append(
                [
                    self.search_number(a[0][0]),
                    self.search_number(a[0][1]),
                    999999
                ]
            )
            a.pop(0)
        return sorted(s)

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self._graph[u].add(v)
        self._graph[v].add(u)
        # find set of an element i

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot  # Make one as root and increment.
            rank[xroot] += 1

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def boruvkaMST(self):
        parent = []
        rank = []
        cheapest = []
        numTrees = self.len_node()
        MSTweight = 0
        if self.check_connected():
            for node in range(self.len_node()):
                parent.append(node)
                rank.append(0)
                cheapest = [-1] * self.len_node()
                # Keep combining components (or sets) until all
            # compnentes are not combined into single MST
            while numTrees > 1:
                for i in range(len(self.new_list())):
                    u, v, w = self.new_list()[i]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        if cheapest[set1] == -1 or cheapest[set1][2] > w:
                            cheapest[set1] = [u, v, w]
                        if cheapest[set2] == -1 or cheapest[set2][2] > w:
                            cheapest[set2] = [u, v, w]
                # Consider the above picked cheapest edges and add them to MST
                for node in range(self.len_node()):
                    if cheapest[node] != -1:
                        u, v, w = cheapest[node]
                        set1 = self.find(parent, u)
                        set2 = self.find(parent, v)
                        if set1 != set2:
                            MSTweight += w
                            self.union(parent, rank, set1, set2)
                            print(
                                "Edge",
                                self.search_key(u),
                                "-",
                                self.search_key(v),
                                "has weight",
                                w,
                                "is included in MST"
                            )
                            numTrees = numTrees - 1

                cheapest = [-1] * self.len_node()
            print("Weight of MST is %d" % MSTweight)
        else:
            print("Graph not connected")

    def new_read(self):
        with open('json/dich.json', 'r',
                  encoding='utf-8') as f:
            text = json.load(f)
            if (text['directed']) == "yes":
                self._directed = True
            else:
                self._directed = False
            s = []
            for i in text["datas"].keys():
                for j in (text["datas"][i].items()):
                    s.append([i, j[0], j[1]])
        return sorted(s)

    def new_print(self):
        print("Graph")
        print(self.print_dir())
        for i in self.new_read():
            print("Node:", i[0], "->", i[1], ": weight =", i[2])

    def node(self):
        node = set()
        with open('json/dich.json', 'r',
                  encoding='utf-8') as f:
            text = json.load(f)
            for i in text["datas"].keys():
                for j in (text["datas"][i].items()):
                    node.add(i)
                    node.add(j[0])
        return sorted(node)

    def num_node(self):
        j = 0
        num_node = defaultdict(set)
        for i in self.node():
            num_node[i].add(j)
            j += 1
        return num_node

    def search_num(self, node):
        return list(self.num_node()[node])[0]

    def search_key(self, value):
        for i, j in (self.num_node().items()):
            if list(j)[0] == value:
                return i

    def new_list(self):
        s = []
        a = (self.new_read())
        while a:
            s.append(
                [
                    self.search_num(a[0][0]),
                    self.search_num(a[0][1]),
                    a[0][2]
                ]
            )
            self.addEdge(a[0][0], a[0][1], a[0][2])
            a.pop(0)
        return sorted(s)

    def len_node(self):
        return len(self.num_node())
