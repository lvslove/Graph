import json


class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w

    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)


class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def new_read(self):
        with open('json/dich.json', 'r',
                  encoding='utf-8') as f:
            text = json.load(f)
            s = []
            for i in text["datas"].keys():
                for j in (text["datas"][i].items()):
                    s.append([i, j[0], j[1]])
        return sorted(s)

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

    def new_list(self):
        a = self.new_read()
        b = self.node()
        while b:
            self.add_vertex(b[0])
            b.pop(0)
        while a:
            self.add_edge(a[0][0], a[0][1], a[0][2])
            a.pop(0)
        return

    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path(edge.sink, sink, path + [edge])
                if result is not None:
                    return result

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path is not None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))


def main():
    g = FlowNetwork()
    g.new_read()
    g.new_list()
    print(g.adj)
    print(g.max_flow('s', 't'))


if __name__ == '__main__':
    main()