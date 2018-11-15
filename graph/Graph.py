class Graph:
    """
    Graph = (V, E)
    V is vertex set, E is edge set
    there is an undirected graph:
    0-1-2
    \/\/
    4-3
    we can get:
        V = [0, 1, 2, 3, 4]
        E = [(0,1), (0,4), (1,0), (1,2), (1,3), (1,4), (2,1), (2,3), (3,1), (3,2), (3,4), (4,0), (4,1), (4,3)]
    such graph, we can express to:
    Adjacency Matrix:
            0 1 2 3 4
          0 0 1 0 0 1
          1 1 0 1 1 1
          2 0 1 0 1 0
          3 0 1 1 0 1
          4 1 1 0 1 0
    Adjacency Table:
        {0: [1, 4], 1: [0, 4, 3, 2], 2: [1, 3], 3: [1, 2, 4], 4: [0, 1, 3]}
    """

    def __init__(self):
        self.table = {}
        self.arr = []
        self.idx = []

    def table_init(self, table):
        self.table = table
        for i in range(len(self.arr)):
            while len(self.arr[i]) < len(table):
                self.arr[i].append(0)
        while len(self.arr) < len(table):
            self.arr.append([0 for _ in range(len(table))])
        for k in table:
            if k not in self.idx:
                self.idx.append(k)
        for k1, v in table.items():
            i1 = self.idx.index(k1)
            for k2 in v:
                i2 = self.idx.index(k2)
                self.arr[i1][i2] = 1

    def array_init(self, arr, idx):
        self.arr = arr
        self.idx = idx
        for i, k1 in enumerate(idx):
            self.table[k1] = self.table.get(k1, [])
            for j, k2 in enumerate(idx):
                if arr[i][j] == 1:
                    if k2 not in self.table[k1]:
                        self.table[k1].append(k2)

    def add_undirected_edge(self, edge):
        self.table[edge[0]] = self.table.get(edge[0], [])
        if edge[1] not in self.table[edge[0]]:
            self.table[edge[0]].append(edge[1])
        self.table[edge[1]] = self.table.get(edge[1], [])
        if edge[0] not in self.table[edge[1]]:
            self.table[edge[1]].append(edge[0])
        self.table_init(self.table)

    def add_directed_edge(self, edge):
        self.table[edge[0]] = self.table.get(edge[0], [])
        self.table[edge[0]].append(edge[1])
        self.table_init(self.table)

    def clear(self):
        self.table = {}
        self.arr = []
        self.idx = []


if __name__ == '__main__':
    table = {0: [1, 4], 1: [0, 2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [0, 1, 3]}
    arr = [[0, 1, 0, 0, 1], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 0]]
    idx = [0, 1, 2, 3, 4]
    g = Graph()

    g.clear()
    g.add_undirected_edge((0, 1))
    g.add_undirected_edge((0, 4))
    g.add_undirected_edge((1, 2))
    g.add_undirected_edge((1, 3))
    g.add_undirected_edge((1, 4))
    g.add_undirected_edge((2, 3))
    g.add_undirected_edge((3, 4))
    print(g.table)

"""
{0: [1, 4], 1: [0, 2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [0, 1, 3]}
"""