"""平衡二叉树，二叉搜索树的改进，又称ALV树
"""
from BinaryTree import BinaryTree


class AVLNode:
    def __init__(self, data, left=None, right=None):
        """
        data: 数据域
        next: 结点指针
        """
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class BBTree(BinaryTree):
    def init(self, arr):
        for i in arr:
            self.insert(i)

    def insert(self, item):
        def recursive(bn):
            if not bn:
                bn = self.node(item)
            elif item < bn.data:  # 插入到左边
                bn.left = recursive(bn.left)
                # 失衡
                if (bn.right and bn.left.height - bn.right.height > 1) or (not bn.right and bn.left.height > 1):
                    if item < bn.left.data:
                        bn = self.ll(bn)
                    else:
                        bn = self.lr(bn)
            else:  # 插入到右边
                bn.right = recursive(bn.right)
                # 失衡
                if (bn.left and bn.right.height - bn.left.height > 1) or (not bn.left and bn.right.height > 1):
                    if item < bn.right.data:
                        bn = self.rl(bn)
                    else:
                        bn = self.rr(bn)

            bn.height = self.height(bn)
            return bn

        if self.is_empty():  # 树为空，作为根结点插入
            self.mid = self.node(item)
        else:
            self.mid = recursive(self.mid)

    def delete(self, item):
        def recursive(bn, key):
            if bn:
                if key == bn.data:  # 找到需要删除的节点
                    if bn.left and bn.right:    # 左右双全
                        if bn.left.height > bn.right.height:
                            p = self.inorder_pre_node(bn)   # 找前驱节点
                            bn.data = p.data    # 替换为前驱节点的值
                            bn.left = recursive(bn.left, p.data)    # 删改的节点变为前驱节点
                        else:
                            p = self.inorder_post_node(bn)
                            bn.data = p.data
                            bn.right = recursive(bn.right, p.data)
                    else:   # 单左或单右或为叶子节点
                        if bn.left:
                            bn = bn.left
                        elif bn.right:
                            bn = bn.right
                        else:
                            return None
                # 失衡
                elif key > bn.data:
                    bn.right = recursive(bn.right, key)
                    if self.is_leaf(bn):
                        pass
                    elif (bn.right and bn.left.height - bn.right.height > 1) or (not bn.right and bn.left.height > 1):
                        if bn.left.left and bn.left.right:
                            if bn.left.left.height > bn.left.right.height:
                                bn = self.ll(bn)
                            else:
                                bn = self.lr(bn)
                        else:
                            if bn.left.left:
                                bn = self.ll(bn)
                            elif bn.left.right:
                                bn = self.lr(bn)
                elif key < bn.data:
                    bn.left = recursive(bn.left, key)
                    if self.is_leaf(bn):
                        pass
                    elif (bn.left and bn.right.height - bn.left.height > 1) or (not bn.left and bn.right.height > 1):
                        if bn.right.left and bn.right.right:
                            if bn.right.left.height > bn.right.right.height:
                                bn = self.rl(bn)
                            else:
                                bn = self.rr(bn)
                        else:
                            if bn.right.left:
                                bn = self.rl(bn)
                            elif bn.right.right:
                                bn = self.rr(bn)

                bn.height = self.height(bn)
                return bn

        assert not self.is_empty(), 'Tree is empty!'

        self.mid = recursive(self.mid, item)

    def inorder_pre_node(self, bn):
        """中序前驱节点"""
        p = bn.left
        if p:
            while p.right:
                p = p.right
            return p

    def inorder_post_node(self, bn):
        """中序后继节点"""
        p = bn.right
        if p:
            while p.left:
                p = p.left
            return p

    def ll(self, bn):
        """ll型，右旋"""
        l = bn.left
        lr = l.right
        l.right = bn
        bn.left = lr
        bn.height = self.height(bn)
        l.height = self.height(l)
        return l

    def rr(self, bn):
        """rr型，左旋"""
        r = bn.right
        rl = r.left
        r.left = bn
        bn.right = rl
        bn.height = self.height(bn)
        r.height = self.height(r)
        return r

    def lr(self, bn):
        """lr型，先左旋，再右旋"""
        bn.left = self.rr(bn.left)
        return self.ll(bn)

    def rl(self, bn):
        """rl型，先右旋，再左旋"""
        bn.right = self.ll(bn.right)
        return self.rr(bn)


if __name__ == '__main__':
    import random

    random.seed(0)

    arr = list(range(1, 11))
    random.shuffle(arr)
    print("输入序列:", arr)
    bt = BBTree(AVLNode)
    bt.init(arr)
    # bt.draw(bt.mid)
    print('广义表形式:', bt.generalized(bt.mid))
    print('树形结构形式:\n', end=bt.tree(bt.mid) + '\n')
    print('中序遍历:', bt.inorder(bt.mid))

    bt.delete(arr[1])
    print('删除 %d 后树状结构:' % arr[1])
    print(bt.tree(bt.mid))
    print('删除后中序遍历:', bt.inorder(bt.mid))

"""
输入序列: [8, 9, 2, 6, 4, 5, 3, 1, 10, 7]
广义表形式: 6(4(2(1,3),5),9(8(7),10))
树形结构形式:
6-->4-->2-->1
        └-->3
    └-->5
└-->9-->8-->7
    └-->10
中序遍历: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
删除 9 后树状结构:
6-->4-->2-->1
        └-->3
    └-->5
└-->8-->7
    └-->10
删除后中序遍历: [1, 2, 3, 4, 5, 6, 7, 8, 10]
"""