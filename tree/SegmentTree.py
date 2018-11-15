from tree.BinaryTree import *


class STree(BTree):
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

    def init(self, arr):
        n = len(arr)
        p = [BNode(None) for _ in range((4 * n))]
        self.build(1, 0, n - 1, p, arr)
        for i in range(len(p) - 1, -1, -1):  # remove the extra site
            if p[i].data is not None:
                break
            p.pop(-1)
        self.n = n
        self.p = p
        self.mid = self.get_mid(p)  # get a tree like structure
        self.array = self.get_array(p)  # get an array like structure
        return True

    def build(self, idx, l, r, p, arr):
        """ recursive
        l, r belong to arr, idx belongs to p
        """
        if l == r:
            p[idx].data = arr[l]
        else:
            mid = (l + r) // 2
            self.build(idx * 2, l, mid, p, arr)
            self.build(idx * 2 + 1, mid + 1, r, p, arr)
            p[idx].data = self.op(p[idx * 2].data, p[idx * 2 + 1].data)

    def op(self, x, y):
        if x is None:
            return y
        elif y is None:
            return x
        else:
            return x + y

    def update(self, val, area):
        if type(area) is int:
            self.update_recursive(1, 0, self.n - 1, area, area, val)
        if type(area) is list:
            self.update_recursive(1, 0, self.n - 1, area[0], area[1], val)

    def update_recursive(self, idx, l, r, a, b, val):
        if r < a or l > b:  # [l, r] is out of [a, b]
            return True
        if l == r:
            self.p[idx].data = val
            return True
        mid = (l + r) // 2
        self.update_recursive(idx * 2, l, mid, a, b, val)
        self.update_recursive(idx * 2 + 1, mid + 1, r, a, b, val)
        self.p[idx].data = self.op(self.p[idx * 2].data, self.p[idx * 2 + 1].data)
        return True

    def query(self, area):
        if type(area) is int:
            return self.query_recursive(1, 0, self.n - 1, area, area)
        if type(area) is list:
            return self.query_recursive(1, 0, self.n - 1, area[0], area[1])

    def query_recursive(self, idx, l, r, a, b):
        if r < a or l > b:
            return None
        if l >= a and r <= b:
            return self.p[idx].data
        mid = (l + r) // 2
        q1 = self.query_recursive(idx * 2, l, mid, a, b)
        q2 = self.query_recursive(idx * 2 + 1, mid + 1, r, a, b)
        return self.op(q1, q2)


if __name__ == '__main__':
    a = list(range(10))
    st = STree()
    st.init(a)

    print('before update: ')
    st.show(st.mid)
    print()

    st.update(10, 0)
    st.update(11, [2, 5])
    print('after update: ')
    st.show(st.mid)
    print()

    print('query area 3 is %d' % st.query(2))
    print('query area [2, 3] is %d' % st.query([1, 2]))

"""
before update: 
45 -- 10 -- 3 -- 1 -- 0
                   |- 1
              |- 2
         |- 7 -- 3
              |- 4
   |- 35 -- 18 -- 11 -- 5
                     |- 6
               |- 7
         |- 17 -- 8
               |- 9
after update: 
85 -- 44 -- 22 -- 11 -- 10
                     |- 1
               |- 11
         |- 22 -- 11
               |- 11
   |- 41 -- 24 -- 17 -- 11
                     |- 6
               |- 7
         |- 17 -- 8
               |- 9
query area 3 is 11
query area [2, 3] is 12
"""
