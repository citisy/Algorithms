"""哈夫曼树，又称最优二叉树
基本特征：叶子带权，带权路径WPL最小
哈夫曼树不唯一"""

from BinaryTree import BinaryTree


class HFNode:
    def __init__(self, data, weight, left=None, right=None):
        """
        data: 数据域
        next: 结点指针
        """
        self.data = data
        self.left = left
        self.right = right
        self.weight = weight


class HTree(BinaryTree):
    """
    functions:
        wpl(len, bn): 计算带权路径长度（WeightPathLength）
        code(bn, length=0): 哈夫曼编码
    """

    def init(self, data_weight):
        """初始化
        :param data_weight: the define of dic is different from which in BTree
                    the k-v of dic means data-weight
        :return:
        """
        t = []
        f = []
        for k, v in data_weight.items():
            t.append(k)
            f.append(v)

        n = len(t)
        t2n = []

        for i in range(n):
            t2n.append(self.node(t[i], f[i]))

        for i in range(n - 1):
            # 选取两个权值最小的点并删除
            k1 = f.index(min(f))  # 最小值的下标
            t1, f1 = t2n.pop(k1), f.pop(k1)

            k2 = f.index(min(f))  # 次最小值的下标
            t2, f2 = t2n.pop(k2), f.pop(k2)

            q = self.node(None, t1.weight + t2.weight)
            q.left = t1
            q.right = t2
            # 把两个点权值之和加入序列中
            t2n.append(q)
            f.append(f1 + f2)
        # print(self.mid) => 哈夫曼树的中序表达
        self.mid = t2n[0]

    def wpl(self, bn, length=0):
        """计算带权路径长度（WeightPathLength）"""
        # 空树返回0
        if bn is None:
            return 0
        # 非空
        else:
            # 左子树和右子树都为空时，返回结点的路径长度
            if not bn.left and not bn.right:
                return bn.weight * length
            # 递归调用
            else:
                return self.wpl(bn.left, length + 1) + self.wpl(bn.right, length + 1)

    def code(self, bn):
        """哈夫曼编码"""

        def recursive(bn, length=0):
            if bn:
                # 叶子结点，打印路径
                if not bn.left and not bn.right:
                    leaf = bn.data
                    h_dic[leaf] = ''
                    for i in range(length):
                        h_dic[leaf] += str(c[i])
                else:
                    #   左孩子编码0
                    c[length] = 0
                    recursive(bn.left, length + 1)
                    # 右孩子编码1
                    c[length] = 1
                    recursive(bn.right, length + 1)

        h_dic = {}
        c = [-1 for _ in range(10)]
        recursive(bn)
        return h_dic


if __name__ == '__main__':
    data_weight = {'a': 4, 'b': 2, 'c': 6, 'd': 8, 'e': 3, 'f': 2}
    print("输入字典:", data_weight)
    bt = HTree(HFNode)
    bt.init(data_weight)
    # bt.draw(bt.mid)
    print('wpl:', bt.wpl(bt.mid))
    print('哈夫曼编码：', bt.code(bt.mid))

"""
输入字典: {'a': 4, 'b': 2, 'c': 6, 'd': 8, 'e': 3, 'f': 2}
wpl: 61
哈夫曼编码：
{'b': '000', 'c': '01', 'd': '11', 'a': '101', 'e': '100', 'f': '001'}
"""
