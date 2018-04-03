# -*- coding: utf-8 -*-

# 哈夫曼树，又称最优二叉树
# 基本特征：叶子带权，带权路径WPL最小
# 哈夫曼树不唯一

import sys
sys.path.append('../link_list')
from BLinkList import BNode
from BTree import BTree


class HTree(BTree):
    '''
    functions:
        wpl(len, bn): 计算带权路径长度（WeightPathLength）
        code(bn, length=0): 哈夫曼编码
    '''

    def __init__(self):
        super(HTree, self).__init__()
        self.c = ['' for _ in range(10)]  # 保存哈夫曼编码用到的数组

    # 初始化
    def init(self, t, f_):
        '''
        :param t: 结点
        :param f: 权值
        :return:
        '''
        n = len(t)
        f = f_[:]  # 转存数组，避免原数组数据被破坏
        # 把序列转换成结点形式
        t2n = []
        for i in range(n):
            t2n.append(BNode([t[i], f[i]]))
            # t2n.append(BNode(t[i]))
        for i in range(n-1):
            # 选取两个权值最小的点并删除
            k1 = f.index(min(f))  # 最小值的下标
            t1 = t2n[k1]
            f1 = f[k1]
            del t2n[k1]
            del f[k1]
            k2 = f.index(min(f))  # 次最小值的下标
            t2 = t2n[k2]
            f2 = f[k2]
            del t2n[k2]
            del f[k2]
            q = BNode(t1.data + t2.data)
            q.left = t1
            q.right = t2
            # 把两个点权值之和加入序列中
            t2n.append(q)
            f.append(f1 + f2)
        # print(self.mid) => 哈夫曼树的中序表达
        self.mid = t2n[0]

    # 计算带权路径长度（WeightPathLength）
    def wpl(self, bn, length=0):
        # 空树返回0
        if bn and bn == '':
            return 0
        # 非空
        else:
            # 左子树和右子树都为空时，返回结点的路径长度
            if not bn.left and not bn.right:
                return bn.data[1] * length
            # 递归调用
            else:
                return self.wpl(bn.left, length+1)+self.wpl(bn.right, length+1)

    # 哈夫曼编码
    def code(self, bn, length=0):
        if bn:
            # 叶子结点，打印路径
            if not bn.left and not bn.right:
                print(bn.data[0], end=': ')
                for i in range(length):
                    print(self.c[i], end=' ')
                print()
            else:
                # 左孩子编码0
                self.c[length] = 0
                self.code(bn.left, length+1)
                # 右孩子编码1
                self.c[length] = 1
                self.code(bn.right, length + 1)


if __name__ == '__main__':
    t = ['a', 'b', 'c', 'd', 'e', 'f']
    f = [4, 2, 6, 8, 3, 2]
    a = [t, f]
    bt = HTree()
    bt.init(t, f)
    print('中序遍历:', bt.mid)
    print('wpl:', bt.wpl(bt.mid))
    print('哈夫曼编码：')
    bt.code(bt.mid)
