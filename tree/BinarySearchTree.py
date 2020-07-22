"""二叉搜索树，又称二叉排序树
基本特征：左孩子<根<右孩子，中序遍历为有序序列
"""

from BinaryTree import BinaryTree


class BSTree(BinaryTree):
    """
    functions:
        insert(item, bn): 插入一个叶子结点
        delete(item, bn): 删除一个结点
    """

    def init(self, arr):
        for i in arr:
            self.insert(i)

    def insert(self, item):
        """非递归插入一个叶子结点"""
        bn = self.node(item)
        if self.is_empty():  # 树为空，作为根结点插入
            self.mid = bn
        else:  # 非空，循环往下查询，较小则往左走，较大则往右走，直至低端
            p = t = self.mid
            while t:
                if item < t.data:
                    p = t
                    t = t.left
                else:
                    p = t
                    t = t.right

            if item < p.data:
                p.left = bn
            else:
                p.right = bn

        return bn

    def delete(self, item):
        """删除一个结点"""

        if self.is_empty():
            print('Tree is empty!')
            return False

        # 循环往下查询，较小则往左走，较大则往右走，直至找到要删除的点
        t = self.mid
        p = t   # t的父节点
        flag = 'm'  # 保存上一步是左走还是右走
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
            print('Can not find item!')
            return False

        if not t.left:  # 根结点左子树为空，将右子树连接该结点对应的位置，子承父业，或其为叶子结点，直接删除
            if flag == 'l':
                p.left = t.right
            elif flag == 'r':
                p.right = t.right

        elif not t.right:  # 根结点右子树为空，将左子树返回该结点对应的位置
            if flag == 'l':
                p.left = t.left
            elif flag == 'r':
                p.right = t.left

        else:  # 左右孩子都不为空时：
            # 找中序前驱结点，即左子树的最右下角结点
            # t2 -> 中序前驱结点, p2 -> t2.parent
            p2 = None
            t2 = t.left
            while t2 and t2.right:
                p2 = t2
                t2 = t2.right

            t.data = t2.data  # 先把要删除的结点的中序前驱结点赋值给该结点

            # 再删除他的中序前驱结点，把其左指针连接到其所在的位置
            if p2:
                p2.right = t2.left
            else:
                t.left = t2.left


if __name__ == '__main__':
    import random

    random.seed(0)

    arr = list(range(1, 11))
    random.shuffle(arr)
    print("输入序列:", arr)
    bt = BSTree()
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
广义表形式: 8(2(1,6(4(3,5),7)),9(,10))
树形结构形式:
8-->2-->1
    └-->6-->4-->3
            └-->5
        └-->7
└-->9
    └-->10
中序遍历: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
删除 9 后树状结构:
8-->2-->1
    └-->6-->4-->3
            └-->5
        └-->7
└-->10
删除后中序遍历: [1, 2, 3, 4, 5, 6, 7, 8, 10]
"""
