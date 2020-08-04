import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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
        self.table = dict()  # {u_node: {v_node}}, weight default 1 or {u_node: {v_node: weight}}
        self.arr = np.zeros((1, 1))  # axis 1: u_node -> 2: v_node
        self.nodes = []
        self.edges = set()  # {u_node, v_node, weight}

    def update_by_edge(self, edge: tuple):
        """输入一条有向边更新"""
        u_node, v_node, weight = edge

        # update edges
        self.edges.add(edge)

        # update nodes
        for node in (u_node, v_node):
            if node not in self.nodes:
                self.nodes.append(node)

        # update table
        self.table[u_node] = self.table.get(u_node, dict())
        self.table[u_node][v_node] = weight

        # update array
        if len(self.nodes) > len(self.arr):
            self.arr = np.pad(self.arr, (0, len(self.nodes) - len(self.arr)), constant_values=0)
        i1, i2 = self.nodes.index(u_node), self.nodes.index(v_node)
        self.arr[i1, i2] = weight

    def get_edges(self) -> list:
        """获取无向边集"""
        edges = []
        cache = []
        for edge in self.edges:
            _ = set(edge[:2])
            if _ not in cache:
                edges.append(edge)
                cache.append(_)
        return edges

    def get_text(self, edges=None, connect=' -- ', weight_fmt='[label="%d"]') -> str:
        """获取文本形式"""
        edges = edges or self.get_edges()
        s = ''
        for edge in edges:
            s += connect.join(edge[:2]) + ' ' + weight_fmt % edge[2] + '\n'

        return s[:-1]

    def update_by_table(self, table: dict):
        """输入邻接表更新"""
        edges = set()
        for u_node, v_nodes in table.items():
            if isinstance(v_nodes, dict):
                for v_node, weight in v_nodes.items():
                    edges.add((u_node, v_node, weight))
            else:
                for v_node in v_nodes:
                    edges.add((u_node, v_node, 1))

        for edge in edges:
            self.update_by_edge(edge)

    def update_by_array(self, arr: np.ndarray, nodes: list):
        """输入邻接矩阵更新"""
        edges = set()

        idx = np.where(arr > 0)
        for _ in range(len(idx[0])):
            i, j = idx[0][_], idx[1][_]
            edges.add((nodes[i], nodes[j], arr[i, j]))

        for edge in edges:
            self.update_by_edge(edge)

    def add_undirected_edge(self, u_node, v_node, weight=1):
        """添加一条无向边"""
        self.update_by_edge((u_node, v_node, weight))
        self.update_by_edge((v_node, u_node, weight))

    def DFS(self):
        """深度优先遍历"""

        def recursive(iu):
            flag[iu] = 1
            for iv in np.where(self.arr[iu] > 0)[0]:
                if not flag[iv]:
                    tree.append((self.nodes[iu], self.nodes[iv], self.arr[iu, iv]))
                    recursive(iv)

        flag = np.zeros_like(self.nodes, dtype=int)
        tree = []
        while 0 in flag:  # 直到所有顶点都被遍历过一遍
            indegree = np.sum(self.arr > 0, axis=0)
            indegree[np.where(flag == 1)] = len(self.nodes) + 1  # 置为最大值
            idx = np.argmin(indegree)
            recursive(idx)

        return tree

    def BFS(self) -> list:
        """广度优先遍历"""

        flag = np.zeros_like(self.nodes, dtype=int)
        tree = []
        while 0 in flag:  # 直到所有顶点都被遍历过一遍
            indegree = np.sum(self.arr > 0, axis=0)
            indegree[np.where(flag == 1)] = len(self.nodes) + 1  # 置为最大值
            idx = np.argmin(indegree)
            queue = [idx]
            flag[idx] = 1
            while queue:
                iu = queue.pop(0)
                for iv in np.where(self.arr[iu] > 0)[0]:
                    if not flag[iv]:
                        tree.append((self.nodes[iu], self.nodes[iv], self.arr[iu, iv]))
                        flag[iv] = 1
                        queue.append(iv)

        return tree

    def min_span_tree(self, method='prim', start_node=None) -> list:
        """最小生成树"""

        def prim() -> list:
            """prim算法"""
            node = start_node or min(self.edges, key=lambda x: x[2])[0]
            u_nodes = {node}
            v_nodes = set(self.nodes) - u_nodes
            tree = []

            while v_nodes:
                cache = []
                for u_node in u_nodes:
                    for v_node in self.table[u_node]:
                        if v_node in v_nodes:
                            cache.append((u_node, v_node, self.table[u_node][v_node]))

                min_edge = min(cache, key=lambda x: x[2])
                u_nodes.add(min_edge[1])
                v_nodes.remove(min_edge[1])

                tree.append(min_edge)

            return tree

        def kruskal() -> list:
            """kruskal算法"""
            node_sets = [{_} for _ in self.nodes]
            edges = sorted(self.edges, key=lambda x: x[2])
            tree = []

            for edge in edges:
                node1, node2 = edge[:2]
                i1 = i2 = -1

                for i, node_set in enumerate(node_sets):
                    if node1 in node_set:
                        i1 = i
                    if node2 in node_set:
                        i2 = i
                    if i1 != -1 and i2 != -1:
                        break

                if i1 != i2:  # 两个顶点分属不同的连通图中，输出这条边，合并两个连通图
                    _ = node_sets.pop(max(i1, i2))
                    node_sets[min(i1, i2)].update(_)
                    tree.append(edge)

            return tree

        methods = {'prim': prim, 'kruskal': kruskal}

        return methods[method]()

    def shortest_path(self, start: str, end: str = None, method='dijkstra') -> (list, float):
        """求最短路径"""

        def dijkstra(start: str, end: str = None) -> (list, float):
            """dijkstra算法"""
            iu = self.nodes.index(start)
            flag = [0] * len(self.nodes)
            flag[iu] = 1

            weight = np.zeros(len(self.nodes)) + np.inf
            weight[iu] = 0
            path = [-1] * len(self.nodes)

            while 0 in flag and self.nodes[iu] != end:
                # 更新权值
                for iv in np.where(self.arr[iu] > 0)[0]:
                    w = self.arr[iu, iv] + weight[iu]
                    if not flag[iv] and w < weight[iv]:
                        weight[iv] = w
                        path[iv] = iu

                # 找最短路径
                # 这一步是可以优化的，例如引入最小堆结构
                for iv in np.argsort(weight):
                    if not flag[iv] and weight[iv] != np.inf:
                        iu = iv
                        flag[iv] = 1
                        break
                else:  # 所有最小权值点都往外扩展过一遍了，说明形成了一个闭环。
                    break

            if self.nodes[iu] != end:  # 起始点和终止点之间不连通
                print('Can not find path!')
                return

            w = weight[iu]
            result = []
            while self.nodes[iu] != start:  # 前溯查找路径
                result.append(self.nodes[iu])
                iu = path[iu]

            result.append(start)

            return result[::-1], w

        def floyed(start: str, end: str = None) -> (list, float):
            """floyed算法"""
            path = np.zeros_like(self.arr, dtype=int) - 1
            path[self.arr > 0] = np.where(self.arr > 0)[0]

            n = len(self.nodes)
            weight = self.arr.copy()
            weight[weight == 0] = np.inf

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if weight[i, k] + weight[k, j] < weight[i, j]:  # 从i经k到j的路径更短
                            weight[i, j] = weight[i, k] + weight[k, j]
                            path[i, j] = path[k, j]

            iu = self.nodes.index(start)
            iv = self.nodes.index(end)
            w = weight[iu, iv]
            result = []

            while self.nodes[iv] != start:  # 前溯查找路径
                result.append(self.nodes[iv])
                iv = path[iu, iv]

            result.append(start)

            return result[::-1], w

        methods = {'dijkstra': dijkstra, 'floyed': floyed}

        return methods[method](start, end)

    def draw(self, edges=None):
        g = nx.Graph()
        g.add_weighted_edges_from(edges or self.get_edges())
        nx.draw(g, with_labels=True)
        plt.show()


def make_a_graph():
    g = Graph()
    arr = np.array([[0, 6, 1, 5, 0, 0],
                    [6, 0, 5, 0, 3, 0],
                    [1, 5, 0, 5, 6, 4],
                    [5, 0, 5, 0, 0, 2],
                    [0, 3, 6, 0, 0, 6],
                    [0, 0, 4, 2, 6, 0]], dtype=int)
    node = ['A', 'B', 'C', 'D', 'E', 'F']
    g.update_by_array(arr, node)
    print('邻接表形式：')
    print(g.table)
    print('边集形式：')
    print(g.get_edges())
    print('文本形式：')
    print(g.get_text())
    # g.draw()

    # edges = g.DFS()[0]
    # edges = g.BFS()[0]
    print('最小生成树：')
    edges = g.min_span_tree(method='prim')
    print(edges)
    # g.draw(edges)

    print(g.shortest_path('A', 'F', method='floyed'))


if __name__ == '__main__':
    make_a_graph()
