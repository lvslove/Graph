import json
from collections import defaultdict

import copy
from typing import List, Any


class Graph(object):

    def __init__(self, directed=False):
        self._directed = directed
        self._graph = defaultdict(set)
        # self.add_connections(connections)

    def nice_print(self):
        s = "\n"
        print("Graph")
        print(self.print_dir())
        for key in self._graph:
            s += '\t{"' + str(key) + '"}:' + str(self._graph[key]) + "\n"

        print(s)

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
        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            print("Node", node, "not exist")
            pass

    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def write_in_file(self):
        s = ""
        for key in self._graph:
            s += '"' + str(key) + '":' + str(self._graph[key]) + ","
        newstring = s
        newstring = newstring.replace('}', ']')
        newstring = newstring.replace("'", '"')
        newstring = newstring.replace('{', '[')
        newstring = newstring.replace('set()', '{}')
        s = "{" + newstring + "}"
        newstring = s[:-2]
        newstring2 = newstring + "}"
        if self._directed:
            newstring3 = "yes"
        else:
            newstring3 = "no"

        d = json.loads(newstring2)
        file_path = 'json/output.json'
        with open(file_path) as f:
            data = json.load(f)
            data['datas'].append(d)
            data['directed'] = newstring3

            with open(file_path, 'w') as outfile:
                json.dump(data, outfile)

    def update_file(self):
        def clear_json():
            file_path = 'json/output.json'
            with open(file_path) as f:
                data = json.load(f)
                data['datas'] = []
                data['directed'] = []

                with open(file_path, 'w') as outfile:
                    json.dump(data, outfile)

        clear_json()
        self.write_in_file()

    def read_json(self):
        with open('json/input.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
            data = json.load(fh)
        if (data['directed']) == "yes":
            self._directed = True
        else:
            self._directed = False
        for value in data['datas']:
            s = value
        z = ""
        for key in value:
            z += '"' + str(key) + '":' + str(value[key]) + ","
        newstring = z
        newstring = newstring.replace('}', ']')
        newstring = newstring.replace("'", '"')
        newstring = newstring.replace('{', '[')
        z = "{" + newstring + "}"
        newstring = z[:-2]
        newstring2 = newstring + "}"
        a = json.loads(newstring2)
        for n in a:
            self.add_Node(n)

            i = 0
            while len(a[n]) > i:
                self.add_Edge(n, a[n][i])
                i += 1

    def print_dir(self):
        if self._directed:
            return "directed"
        else:
            return "undirected"

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

    def task3(self, g2):
        if g2._graph.items() == self._graph.items():
            print(True)
            print("Graps match")
        else:
            print(False)
            print("Graps no match")

    def dfs(self, node, time, visited=None, entry=None, leave=None):
        time += 1
        entry[node].add(time)

        if visited is None:
            visited = set()
        visited.add(node)
        #print(node)
        for nxt in self._graph[node] - visited:
            self.dfs(nxt, time, visited, entry, leave)
        time += 1
        leave[node].add(time)

    def invert_list(self, g2):
        s = []
        print("invert Graph")
        for i in self._graph.keys():
            if self._graph[i] == set():
                g2.add_Node(i)
            else:
                for j in self._graph[i]:
                    g2.add_Edge(j, i)
        return g2.nice_print()

    def all_nodes(self):
        s = []
        for i in self._graph.keys():
            s.append(i)
            for j in self._graph[i]:
                s.append(j)
        woduplicates = set(s)
        return woduplicates

    def key_val(self):
        i = 0
        d = defaultdict(set)
        for j in self.all_nodes():
            d[i].add(j)
            i += 1
        return d

    def list_sm(self):
        s = []
        d = self.key_val()
        adj = [[] for i in range(len(self.all_nodes()))]
        for i in self._graph.keys():
            for j in self._graph[i]:
                s.append((i, j))
                adj[int(i)-1].append(int(j)-1)
        return adj
        #return s

    def list_sm2(self):
        s = []
        d = self.key_val()
        #print(d)
        adj = [[] for i in range(len(self.all_nodes()))]
        for i in self._graph.keys():
            for j in self._graph[i]:
                s.append((i, j))
        for z in d.keys():
                    #print(z)
            for y in d[z]:
                print(z,y)

        return adj


    def list_invert(self):
        s = []
        adjT = [[] for i in range(len(self.all_nodes()))]
        for i in self._graph.keys():
            for j in self._graph[i]:
                s.append((int(i), int(j)))
                adjT[int(j) - 1].append(int(i) - 1)
        return adjT



