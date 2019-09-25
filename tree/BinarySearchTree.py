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
        p = t
        flag = 'm'  # 保存下一步是左走还是右走
        while t:  # t -> 要删除的结点
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
            print('can not find item!')
            return

        # if t.left is None and t.right is None:
        #
        if t.left is None:      # 根结点左子树为空，将右子树连接该结点对应的位置，或其为叶子结点，直接删除
            if flag == 'l':
                p.left = t.right
            elif flag == 'r':
                p.right = t.right

        elif t.right is None:   # 根结点右子树为空，将左子树返回该结点对应的位置
            if flag == 'l':
                p.left = t.left
            elif flag == 'r':
                p.right = t.left

        else:    # 左右孩子都不为空时：
            # 找中序前驱结点，即左子树的最右下角结点
            # t2 -> 中序前驱结点, p2 -> t2.parent
            p2 = None
            t2 = t.left
            while t2:
                if t2.right:
                    p2 = t2
                    t2 = t2.right
                else:
                    break
            t.data = t2.data    # 先把要删除的结点的中序前驱结点赋值给该结点
            if p2 is None:  # 再删除他的中序前驱结点，把其左指针连接到其所在的位置
                t.left = t2.left
            else:
                p2.right = t2.left


if __name__ == '__main__':
    import random

    arr = list(range(1, 11))
    random.shuffle(arr)

    bt = BSTree()
    bt.init(arr)

    print('广义表:', end=' ')
    bt.print_(bt.mid)
    print()

    print('树状结构：')
    bt.show(bt.mid)
    print()

    print('中序遍历:', end=' ')
    bt.init_order()
    bt.inorder(bt.mid)
    print(bt.order)

    print()
    bt.delete(arr[1])
    print('删除 %d 后树状结构:' % arr[1])
    bt.show(bt.mid)
    print()

    print('删除后中序遍历:', end=' ')
    bt.init_order()
    bt.inorder(bt.mid)
    print(bt.order)

"""
广义表: 1(,9(3(2,7(4(,5(,6)),8)),10))
树状结构：
1 -- 
  |- 9 -- 3 -- 2
            |- 7 -- 4 -- 
                      |- 5 -- 
                           |- 6
                 |- 8
       |- 10
中序遍历: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

删除 9 后树状结构:
1 -- 
  |- 8 -- 3 -- 2
            |- 7 -- 4 -- 
                      |- 5 -- 
                           |- 6
       |- 10
删除后中序遍历: [1, 2, 3, 4, 5, 6, 7, 8, 10]
"""
