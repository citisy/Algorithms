# -*- coding: utf-8 -*-

# 二叉搜索树，又称二叉排序树
# 基本特征：左孩子<根<右孩子

import sys
sys.path.append('../link_list')
from BLinkList import BNode
from BTree import BTree

class BSTree(BTree):
    '''
    inserst(item, bn): 插入一个结点
    delete(item, bn): 删除一个结点
    '''

    # 插入一个结点
    # 非递归
    def inserst(self, item, bn):
        if self.is_empty():
            self.mid = BNode(item)
        else:
            t = self.mid
            # 循环往下查询，较小则往左走，较大则往右走，直至低端
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
    def delete(self, item, bn):
        pass

if __name__ == '__main__':
    arr = [38, 26, 62, 94, 35, 50, 28, 55]
    bt = BSTree()
    for i in arr:
        bt.inserst(i, bt.mid)
    bt.print_(bt.mid)
