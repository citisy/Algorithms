from Graph import *


class DiGraph(Graph):
    def add_edge(self, u_node, v_node, weight=1, weight_uv=None, weight_vu=None):
        """添加一条双向边"""
        self.update_by_edge((u_node, v_node, weight_uv or weight))
        self.update_by_edge((v_node, u_node, weight_vu or weight))

    def add_directed_edge(self, u_node, v_node, weight=1):
        """添加一条有向边"""
        self.update_by_edge((u_node, v_node, weight))

    def get_edges(self) -> list:
        return self.edges

    def get_text(self, edges=None, connect=' -> ', weight_fmt='[label="%d"]') -> str:
        return super().get_text(edges, connect, weight_fmt)

    def min_span_tree(self, start_node=None, **kwargs) -> list:
        """最小树型图
        start_node: 如果不指定该参数，则为不定根的最小树型图
        todo: 返回的是最小生成树的路径长度，后面找时间改成返回最短路径"""
        g = DiGraph()
        g.update_by_array(self.arr, self.nodes)
        m = 0
        if start_node is None:
            m = sum([i[2] for i in g.edges]) + 1
            g.update_by_table({None: {k: m for k in g.nodes}})

        i0 = g.nodes.index(start_node)

        arr = g.arr
        arr[arr == 0] = np.inf

        n = len(g.nodes)

        flag = [0] * n  # 用于保存是否为收缩点的标志
        path = [-1] * n
        path[i0] = i0

        s = 0
        while True:
            # 求最短入边集
            for i in range(n):
                if flag[i] or i == i0:
                    continue

                path[i] = i
                for j in range(n):
                    if not flag[j] and arr[j, i] < arr[path[i], i]:
                        path[i] = j
                if path[i] == i:
                    return []

            # 检测是否有环
            for i in range(n):
                if flag[i] or i == i0:
                    continue

                # 判断当前顶点是否有环
                visited = [0] * n
                j = i
                while True:
                    visited[j] = 1
                    j = path[j]
                    if visited[j]:  # 从j开始有环或无环
                        break

                if j == i0:  # 当前顶点无环
                    continue

                # 保存有向环的路径
                i = j  # 保存有向环的起点
                cache = []
                while True:
                    cache.append(j)
                    j = path[j]
                    if j == i:
                        break

                # 保存权值
                for j in cache:
                    s += arr[path[j], j]

                # 修改权值
                for j in cache:
                    for k in range(n):
                        if not flag[k] and arr[k][j] != np.inf and k != path[j]:
                            arr[k][j] -= arr[path[j]][j]

                # 缩点
                for j in range(n):
                    if j == i:
                        continue

                    for k in cache[1:]:
                        if arr[k, j] < arr[i, j]:
                            arr[i, j] = arr[k, j]
                        if arr[j, k] < arr[j, i]:
                            arr[j, i] = arr[j, k]

                # 设置前序顶点
                for j in cache[1:]:
                    flag[j] = 1

                break

            # 所有点都检查过，不存在环
            if i == n - 1:
                for i in range(n):
                    if not flag[i] and i != i0:
                        s += arr[path[i], i]
                break

        return s - m

    def topological_sort(self) -> list:
        """拓扑排序"""
        indegree = np.sum(self.arr > 0, axis=0)
        idx = np.where(indegree == 0)  # 查找入度为0的点
        stack = list(idx[0])  # 然后入队
        indegree[idx] = -1  # 已经入队的点入度置为-1，后面就不会再遍历了
        r = []

        while stack:
            iu = stack.pop(0)
            r.append(iu)
            indegree = indegree - (self.arr[iu] > 0)  # 删掉遍历点对其他点的入度
            idx = np.where(indegree == 0)
            stack += list(idx[0])
            indegree[idx] = -1

        if len(r) < len(self.nodes):
            return []

        return [self.nodes[_] for _ in r]

    def critical_path(self) -> list:
        """关键活动"""
        order = self.topological_sort()
        if not order:
            return []

        # order = [self.nodes.index(i) for i in order]
        n = len(order)

        # 更新最早发生时间
        ve = [0] * n
        for i0 in range(n):
            k0 = order[i0]
            if k0 not in self.table:
                continue
            for k1, v in self.table[k0].items():
                i1 = order.index(k1)
                ve[i1] = max(ve[i1], ve[i0] + v)

        # 更新最迟发生时间
        vl = [ve[n - 1] for _ in range(n)]
        for i0 in range(n - 1, -1, -1):
            k0 = order[i0]
            if k0 not in self.table:
                continue
            for k1, v in self.table[k0].items():
                i1 = order.index(k1)
                vl[i0] = min(vl[i0], vl[i1] - v)

        # 判断关键活动
        edges = []
        for i0 in range(n):
            k0 = order[i0]
            if k0 not in self.table:
                continue
            for k1, v in self.table[k0].items():
                i1 = order.index(k1)
                if ve[i0] == vl[i1] - v:
                    edges.append((k0, k1, v))

        return edges

    def draw(self, edges=None):
        g = nx.DiGraph()
        g.add_weighted_edges_from(edges or self.edges)
        nx.draw(g, with_labels=True)
        plt.show()


def make_a_AOE():
    g = DiGraph()
    g.add_directed_edge('v0', 'v1', 6)
    g.add_directed_edge('v0', 'v2', 4)
    g.add_directed_edge('v0', 'v3', 5)
    g.add_directed_edge('v1', 'v4', 1)
    g.add_directed_edge('v2', 'v4', 1)
    g.add_directed_edge('v3', 'v5', 2)
    g.add_directed_edge('v4', 'v6', 9)
    g.add_directed_edge('v4', 'v7', 7)
    g.add_directed_edge('v5', 'v7', 4)
    g.add_directed_edge('v6', 'v8', 2)
    g.add_directed_edge('v7', 'v8', 4)

    # g.draw()
    print(g.get_text())
    print(g.topological_sort())
    print(g.critical_path())


def make_a_di_graph():
    g = DiGraph()
    arr = np.array([[0, 9, 0, 0, 5, 0, 0],
                    [0, 0, 3, 9, 0, 0, 0],
                    [0, 7, 0, 0, 0, 9, 6],
                    [3, 0, 8, 0, 0, 5, 0],
                    [0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 0, 3, 0, 4],
                    [0, 0, 4, 0, 0, 8, 0]])
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    g.update_by_array(arr, nodes)
    print(g.get_text())
    # g.draw()
    edges = g.DFS()
    print(edges)
    # g.draw(edges)
    edges = g.BFS()
    print(edges)
    # g.draw(edges)
    print(g.min_span_tree())

    print(g.shortest_path('A', 'G', method='dijkstra'))

    print(g.topological_sort())


if __name__ == '__main__':
    make_a_AOE()
