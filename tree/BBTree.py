"""平衡二叉树，二叉搜索树的改进，又称ALV树
基本特征：比一般的结点多了两个域，左右线索域，取真时指向线索，取假时指向孩子
"""

from tree.BTree import *

class TTNode(BNode):
    def __init__(self, ltag=0, rtag=0):
        super(TTNode, self).__init__()
        self.ltag = ltag
        self.rtag = rtag


class BBTree(BTree):
    '''
    inserst(item, bn): 插入一个结点
    delete(item, bn): 删除一个结点
    '''

    # 初始化
    def init(self):
        pass

    # 插入一个结点
    def inserst(self, item, bn):
        pass

    # 删除一个结点
    def delete(self, item, bn):
        pass