import json
from collections import defaultdict


class Graph(object):

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def nice_print(self ):
        s="\n"
        print(self._directed)
        for key in self._graph:
            s+='\t{"'+str(key)+'"}:'  + str(self._graph[key])+"\n"


        print(s)

    def test(self):
        print (self._directed)

    def add_connections(self, connections):

        for node1, node2 in connections:
            self.add_Edge(node1, node2)

    def add_Edge(self, node1, node2):

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def add_Node(self, node1):
        self._graph[node1]


    def remove_Edge(self, node1, node2):


        self._graph[node1].remove(node2)
        if not self._directed:
            self._graph[node2].remove(node1)

    def remove_Node(self, node):


        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]



    def write_in_file(self):
        s = ""
        for key in self._graph:

            s+= '"'+str(key)+'":' + str(self._graph[key])+","

        newstring = s
        newstring = newstring.replace('}', ']')
        newstring = newstring.replace("'", '"')
        newstring = newstring.replace('{', '[')
        newstring = newstring.replace('set()', '{}')
        s = "{" + newstring + "}"
        newstring = s[:-2]
        newstring2 = newstring + "}"
        print(newstring2)
        if self._directed:
            newstring3 = "yes"
        else:
            newstring3 = "no"

        d = json.loads(newstring2)
        file_path = 'file.json'
        with open(file_path) as f:
            data = json.load(f)
            data['datas'].append(d)
            data['directed'] = newstring3

            with open(file_path, 'w') as outfile:
                json.dump(data, outfile)


    def update_file(self):
        def clear_json():
            file_path = 'file.json'
            with open(file_path) as f:
                data = json.load(f)
                data['datas'] = []
                data['directed'] = []

                with open(file_path, 'w') as outfile:
                    json.dump(data, outfile)
        clear_json()
        self.write_in_file()

    def read_json(self):
        with open('creat.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
            data = json.load(fh)
        if (data['directed'])=="yes":
            self._directed=True
        else:
            self._directed=False
        for value in data['datas']:
           s=(value)
        print(s)
        z=""
        for key in value:

            z+= '"'+str(key)+'":' + str(value[key])+","
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
            i=0
            while(len(a[n])>i):
                self.add_Edge(n,a[n][i])
                i+=1

