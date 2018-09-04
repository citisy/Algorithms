"""线索二叉树，线索化的二叉树
基本特征：比一般二叉树增加两个域：ltag和rtag，child为空是tag=1，child指向对应（前驱或后继）节点
"""


class BNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.ltag = 0
        self.rtag = 0


class TTree:
    """
    inserst(item, bn): 插入一个结点
    delete(item, bn): 删除一个结点
    """

    def __init__(self):
        self.mid = None  # middle node or root node

    # 初始化
    def init(self, arr):
        """
        :param arr: list, item index begin at 1, empty item filled with ''
        """
        if arr[0] != 'flag':
            print('array must be start from the index of 1!')
            return -1
        if not self.is_empty():
            print('array is not empty!')
            return -1
        else:
            self.mid = BNode(arr[1])
            # 二叉链表的存储映象
            # even is left, odd is right, and 1 is mid node
            p = [BNode(None) for _ in range(len(arr))]
            p[1] = self.mid
            for i in range(2, len(arr)):
                if arr[i] == '':
                    continue
                # 左孩子
                if i % 2 == 0:
                    self.lappend(arr[i], p[i // 2])
                    p[i] = p[i // 2].left
                # 右孩子
                else:
                    self.rappend(arr[i], p[i // 2])
                    p[i] = p[i // 2].right
        self.pre = self.mid
        self.thread(self.mid)
        self.pre.right = self.mid
        self.pre.rtag = 1
        print('init successfully!')
        return 1

    def thread(self, bn):
        if bn:
            self.thread(bn.left)
            if bn.left is None:  # left is empty, point to precursor node
                bn.left = self.pre
                bn.ltag = 1
            if self.pre.right is None:  # right is empty, point to successor node
                self.pre.right = bn
                self.pre.rtag = 1
            self.pre = bn
            self.thread(bn.right)

    def inorder(self, bn):
        if bn:
            if bn.ltag == 0:
                self.inorder(bn.left)
            self.order.append([bn.data, bn.ltag, bn.rtag, bn.left.data, bn.right.data])
            if bn.rtag == 0:
                self.inorder(bn.right)

    def init_order(self):
        self.order = []

    def is_empty(self):
        return self.mid is None

    # 当前结点的右指针添加一个结点
    def rappend(self, item, bn):
        # 链表为空
        if self.is_empty():
            self.mid = BNode(item)
        else:
            newp = BNode(item)
            bn.right = newp

    # 左指针添加一个结点
    def lappend(self, item, bn):
        # 链表为空
        if self.is_empty():
            self.mid = BNode(item)
        else:
            newp = BNode(item)
            bn.left = newp

    # 插入一个结点
    def inserst(self, item, bn):
        pass

    # 删除一个结点
    def delete(self, item, bn):
        pass


if __name__ == '__main__':
    a = ['' for _ in range(15)]
    item = ['flag', 'a', 'b', 'e', 'c', 'd', 'f', 'g']
    index = [0, 1, 2, 3, 4, 5, 7, 14]
    k = 0
    for i in index:
        a[i] = item[k]
        k += 1

    tt = TTree()
    tt.init(a)
    tt.init_order()

    tt.inorder(tt.mid)
    print(tt.order)

"""
init successfully!
[['c', 1, 1, 'a', 'b'], ['b', 0, 0, 'c', 'd'], ['d', 1, 1, 'b', 'a'], ['a', 0, 0, 'b', 'e'], ['e', 1, 0, 'a', 'f'], ['g', 1, 1, 'e', 'f'], ['f', 0, 1, 'g', 'a']]
"""
