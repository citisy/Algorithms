"""二叉搜索树，又称二叉排序树
基本特征：左孩子<根<右孩子，中序遍历为有序序列
"""

from tree.BinaryTree import *


class BSTree(BTree):
    """
    functions:
        insert(item, bn): 插入一个叶子结点
        delete(item, bn): 删除一个结点
    """

    def init(self, arr):
        for i in arr:
            self.insert(i)

    # 插入一个叶子结点
    # 非递归
    def insert(self, item):
        # 树为空，作为根结点插入
        if self.is_empty():
            self.mid = BNode(item)
        # 非空
        else:
            # 循环往下查询，较小则往左走，较大则往右走，直至低端
            t = self.mid
            while t:
                if item < t.data:
                    p = t
                    t = t.left
                else:
                    p = t
                    t = t.right
            if item < p.data:
                p.left = BNode(item)
            else:
                p.right = BNode(item)

    # 删除一个结点
    def delete(self, item):
        if self.is_empty():
            print('tree is empty!')
            return
        # 循环往下查询，较小则往左走，较大则往右走，直至找到要删除的点
        t = self.mid
        flag = 'm'  # 保存下一步是左走还是右走
        # t=>要删除的结点
        while t:
            if item < t.data:
                p = t
                t = t.left
                flag = 'l'
            elif item > t.data:
                p = t
                t = t.right
                flag = 'r'
            else:
                break
        if t is None:
            print('cant find item!')
            return
        # 根结点左子树为空，将右子树连接该结点对应的位置，或其为叶子结点，直接删除
        if t.left is None:
            if flag == 'l':
                p.left = t.right
            elif flag == 'r':
                p.right = t.right
        # 根结点右子树为空，将左子树返回该结点对应的位置
        elif t.right is None:
            if flag == 'l':
                p.left = t.left
            elif flag == 'r':
                p.right = t.left
        # 左右孩子都不为空时：
        else:
            # 找中序前驱结点，即左子树的最右下角结点
            # t2=>中序前驱结点
            t2 = t.left
            while t2:
                if t2.right:
                    p2 = t2
                    t2 = t2.right
                else:
                    break
            # 先把要删除的结点的中序前驱结点赋值给该结点
            t.data = t2.data
            # 再删除他的中序前驱结点，把其左指针连接到其所在的位置
            p2.right = t2.left



if __name__ == '__main__':
    arr = [38, 26, 62, 94, 35, 50, 28, 55]
    bt = BSTree()
    bt.init(arr)

    print('广义表:', end=' ')
    bt.print_(bt.mid)
    print()

    print('中序遍历:', end=' ')
    bt.init_order()
    bt.inorder(bt.mid)
    print(bt.order)

    bt.delete(38)
    print('删除后广义表:', end=' ')
    bt.print_(bt.mid)
    print()

    print('删除后中序遍历:', end=' ')
    bt.init_order()
    bt.inorder(bt.mid)
    print(bt.order)

"""
广义表: 38(26(,35(28)),62(50(,55),94))
中序遍历: [26, 28, 35, 38, 50, 55, 62, 94]
删除后广义表: 35(26(,28),62(50(,55),94))
删除后中序遍历: [26, 28, 35, 50, 55, 62, 94]
"""