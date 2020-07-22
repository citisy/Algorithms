from BinaryTree import BinaryTree


class STree(BinaryTree):
    """
    about structure of tree:
        there is an array: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        there is Segment Tree base on the array:
                     45
                 /      \
               10       35
             /  \      / \
            3   7    18  17
           /\  /\   /\  /\
          1 2 3 4 11 7 8 9
         /\      /\
        0 1     5 6

        the item in the array become the tree's leaves,
        their parent is whose children's operation
        here, i define the sum operation,
        also, u can rewrite the function op() to define the tree's operation
    about num of node:
        if it's a full binary tree, which depth is h, it only needs 2^h-1 nodes, it almost is len(array)*2
        but it's a self-balancing binary search tree, so it needs len(array)*2*2 nodes
    """

    def __init__(self, operate=None):
        super().__init__()
        self.op = operate or self.sum_op

    def init(self, arr):
        def recursive(idx, l, r, p):
            """ recursive
            l, r belong to arr, idx belongs to p
            """
            if l == r:  # 说明输入只有一个元素
                p[idx].data = arr[l]
            else:
                mid = (l + r) // 2
                recursive(idx * 2, l, mid, p)
                recursive(idx * 2 + 1, mid + 1, r, p)
                p[idx].data = self.op(p[idx * 2].data, p[idx * 2 + 1].data)

        n = len(arr)
        p = [self.node(None) for _ in range((4 * n))]
        recursive(1, 0, n - 1, p)

        for i in range(len(p) - 1, -1, -1):  # remove the extra memory
            if p[i].data is not None:
                break
            p.pop(-1)

        self.n = n
        self.p = p
        self.mid = self.get_mid(p)  # get a tree like structure
        self.array = self.get_array(self.mid)  # get an array like structure

    def sum_op(self, x, y):
        if x is None:
            return y
        elif y is None:
            return x
        else:
            return x + y

    def update(self, value, i=None):
        def recursive(idx, l, r, value, i):
            if r < i or l > i:  # a not in [l, r]
                return
            if l == r:
                self.p[idx].data = value
                return
            mid = (l + r) // 2
            recursive(idx * 2, l, mid, value, i)
            recursive(idx * 2 + 1, mid + 1, r, value, i)
            self.p[idx].data = self.op(self.p[idx * 2].data, self.p[idx * 2 + 1].data)
            return True

        if isinstance(value, dict):
            for k, v in value.items():
                recursive(1, 0, self.n - 1, v, k)
            return True
        else:
            return recursive(1, 0, self.n - 1, value, i)

    def query(self, l, r=None):
        def recursive(idx, l, r, a, b):
            if r < a or l > b:
                return None
            if a <= l <= r <= b:  # 查询区间包含当前节点的区间，返回当前节点
                return self.p[idx].data
            mid = (l + r) // 2
            q1 = recursive(idx * 2, l, mid, a, b)
            q2 = recursive(idx * 2 + 1, mid + 1, r, a, b)
            return self.op(q1, q2)

        if r:
            return recursive(1, 0, self.n - 1, l, r)
        else:
            return recursive(1, 0, self.n - 1, 0, l)


if __name__ == '__main__':
    a = list(range(10))
    print("输入序列:", a)
    st = STree()
    st.init(a)
    print('构建的线索树:\n', end=st.tree(st.mid) + '\n')
    # st.draw(st.mid)
    print('query area [2, 5] is %d' % st.query(2, 5))
    st.update(10, 0)
    st.update({1: 9, 2: 8})
    print('after update:\n', end=st.tree(st.mid) + '\n')

"""
输入序列: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
构建的线索树:
45-->10-->3-->1-->0
              └-->1
          └-->2
      └-->7-->3
          └-->4
 └-->35-->18-->11-->5
                └-->6
           └-->7
      └-->17-->8
           └-->9
query area [2, 5] is 14
after update:
85-->44-->22-->11-->10
                └-->1
           └-->11
      └-->22-->11
           └-->11
 └-->41-->24-->17-->11
                └-->6
           └-->7
      └-->17-->8
           └-->9
"""
