"""中序线索二叉树，线索化的二叉树
基本特征：比一般二叉树增加两个域：ltag和rtag，child为空时tag=1，child指向对应（前驱或后继）节点
"""
from BinaryTree import BinaryTree


class TTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.ltag = 0
        self.rtag = 0


class TTree(BinaryTree):
    """
    insert(item, bn): 插入一个结点
    delete(item, bn): 删除一个结点
    """

    def init(self, dic):
        """初始化"""
        super(TTree, self).init(dic)
        self.head = self.node(None, left=self.mid)  # 带头节点的树
        self.thread(self.mid)

    def thread(self, bn):
        def recursive(bn):
            global pre
            if bn:
                recursive(bn.left)
                if not bn.left:  # left is empty, point to precursor node
                    bn.left = pre
                    bn.ltag = 1
                if not pre.right:  # right is empty, point to successor node
                    pre.right = bn
                    pre.rtag = 1
                pre = bn
                recursive(bn.right)

        global pre
        pre = self.head
        recursive(bn)
        pre.right = self.head
        pre.rtag = 1

    def inorder(self, bn: TTNode):
        order = []
        p = self.head.left
        while p is not self.head:
            while not p.ltag:
                p = p.left
            order.append([p.data, [p.left.data, p.ltag], [p.right.data, p.rtag]])
            while p.rtag and p.right is not self.head:
                p = p.right
                order.append([p.data, [p.left.data, p.ltag], [p.right.data, p.rtag]])
            p = p.right

        return order


if __name__ == '__main__':
    index_item = {1: 'a', 2: 'b', 3: 'e', 4: 'c', 5: 'd', 7: 'f', 14: 'g'}
    tt = TTree(TTNode)
    tt.init(index_item)
    print('中序遍历:', tt.inorder(tt.mid))

"""
中序遍历: [['c', [None, 1], ['b', 1]], ['b', ['c', 0], ['d', 0]], ['d', ['b', 1], ['a', 1]], ['a', ['b', 0], ['e', 0]], ['e', ['a', 1], ['f', 0]], ['g', ['e', 1], ['f', 1]], ['f', ['g', 0], [None, 1]]]
"""
