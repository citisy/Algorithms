"""
根据数组创建一个应用双链表的二叉树
二叉树的种类：
    满二叉树：每一层都是满的
    完全二叉树：除最后一层或包括最后一层，其余层全满，最后一层在右边缺若干个结点
    理想平衡二叉树：除最后一层或包括最后一层，其余层全满，最后一层的结点任意分布
种类包含情况：
    理想平衡二叉树>完全二叉树>满二叉树
二叉树的一些特征：
    叶子结点n0，单分支n1，双分支n2
        => n0+n1+n2=n1+2n2+1
        => n0=n2+1
        => 叶子结点比双分支结点多1个
    根结点：i 左孩子：2i 右孩子：2i+1
    n个结点的完全二叉树的深度：lb(n)+1（下取整）
"""

from link_list.BLinkList import BNode, BLinkList
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.collections as plc


class BinaryTree(BLinkList):
    """
    functions：
        init(arr): 初始化树
        print_(bn): 打印出二叉树的广义表
        inorder(bn): 中序遍历
        preorder(bn): 前序遍历
        postorder(bn): 后序遍历
        depth(bn): 返回树的深度
        find(item, bn): 查找某一元素是否存在
        get_bn(): 获取当前结点
        update(item, change_item, bn): 更新一个结点
    """

    def init(self, dic):
        if not self.is_empty():
            print('The present tree is not empty!')
            return False

        max_len = max(dic.values())
        arr = [None for _ in range(max_len + 1)]

        for k, v in dic.items():
            arr[v] = k

        self.mid = BNode(arr[1])
        # 二叉链表的存储映象
        # even is left child, odd is right child, and 1 is mid node
        p = [BNode(None) for _ in range(len(arr))]  # don't use `[BNode(None)] * len(arr)`
        for i in range(1, len(arr)):
            if arr[i] is not None:
                p[i].data = arr[i]

        self.p = p
        self.mid = self.get_mid(p)
        self.array = [_.data for _ in p]
        print('init successfully!')
        return True

    def restore_tree(self, in_order: list, pre_order: list = None, post_order: list = None):
        """输入中序序列以及先序或后序序列，还原二叉树"""
        if not in_order:
            print('You must input in_order!')
            return False

        if not (pre_order or post_order):
            print('You input neither pre_order nor post_order!')
            return False

        if not self.is_empty():
            print('The present tree is not empty!')
            return False

        order = pre_order or post_order[::-1]
        if len(in_order) != len(order):
            print('Input order must have the same length!')
            return False

        self.mid = BNode(order[0])

        flag = [0] * len(in_order)  # 标记数组
        p = [BNode(None) for _ in range(len(in_order))]  # 存储映像
        idx = in_order.index(order[0])
        flag[idx] = 1
        p[idx] = self.mid

        for d in order[1:]:
            idx = in_order.index(d)
            p[idx].data = d

            if not sum(flag[:idx]):  # 最左边
                f_idx = flag.index(1)
                p[f_idx].left = p[idx]

            elif not sum(flag[idx + 1:]):  # 最右边
                f_idx = -flag[::-1].index(1) - 1
                p[f_idx].right = p[idx]

            else:  # 两标记元素的中间
                l_idx = idx - flag[:idx][::-1].index(1) - 1  # 最靠近当前节点左边的节点
                r_idx = idx + flag[idx + 1:].index(1) + 1  # 最靠近当前节点右边的节点

                if pre_order:
                    if not p[l_idx].right:  # 不存在右子树
                        p[l_idx].right = p[idx]
                    else:  # 存在右子树
                        p[r_idx].left = p[idx]
                else:
                    if not p[r_idx].left:  # 不存在右子树
                        p[r_idx].left = p[idx]
                    else:  # 存在右子树
                        p[l_idx].right = p[idx]

            flag[idx] = 1

        self.array = self.get_array(self.mid)
        self.p = [BNode(_) for _ in self.array]
        return True

    def generalized(self, bn):
        """返回二叉树的广义表"""

        def recursive(bn):
            if bn:
                stack.append(str(bn.data))
                if bn.left or bn.right:
                    stack.append('(')  # 存在左或右孩子时打印'('
                    recursive(bn.left)
                    if bn.right:
                        stack.append(',')  # 存在右孩子时打印','
                        recursive(bn.right)
                    stack.append(')')  # 左右孩子都遍历完，打印')'

        stack = []
        recursive(bn)
        return ''.join(stack)

    def tree(self, bn):
        """返回二叉树的树形结构"""

        def recursive(bn, dep=0, length=[]):
            if bn:
                stack.append(str(bn.data))
                if bn.left or bn.right:
                    if dep >= len(length):
                        length.append(len(str(bn.data)))
                    else:
                        length[dep] = max(length[dep], len(str(bn.data)))
                    dep += 1
                    stack.append('-->')
                    recursive(bn.left, dep, length)
                    if bn.right:
                        s = ''
                        for i in range(dep):
                            s += ' ' * (length[i] + 3)
                        stack.append('\n%s└-->' % s[:-4])
                        recursive(bn.right, dep, length)
            else:
                stack.pop(-1)

        stack = []
        recursive(bn)
        return ''.join(stack)

    def draw(self, bn):
        """图像可视化"""
        array = self.get_array(bn)
        fig, ax = plt.subplots()
        r = 1
        max_depth = self.depth(bn)
        max_width = 2 ** (max_depth - 1) * 3 * r
        circles, lines = [], []
        get_xy = lambda depth, i: (max_width * (2 * i + 1) / 2 ** (depth + 1), -max_width * depth / max_depth / 2)

        for depth in range(max_depth):
            for i, data in enumerate(array[2 ** depth: 2 ** (depth + 1)]):
                if data:
                    x, y = get_xy(depth, i)
                    circles.append(mpatches.Circle((x, y), r))
                    ax.text(x, y, data, ha='center', va='center', size=15)
                    if 2 ** (depth + 1) + 2 * i < len(array) and array[2 ** (depth + 1) + 2 * i]:  # 有左子树
                        lines.append(((x, y), get_xy(depth + 1, 2 * i)))
                    if 2 ** (depth + 1) + 2 * i + 1 < len(array) and array[2 ** (depth + 1) + 2 * i + 1]:  # 有右子树
                        lines.append(((x, y), get_xy(depth + 1, 2 * i + 1)))

        pc = plc.PatchCollection(circles)
        lc = plc.LineCollection(lines)
        ax.add_collection(pc, autolim=True)
        ax.add_collection(lc, autolim=True)
        ax.autoscale_view()
        ax.set_axis_off()
        plt.axis('equal')
        plt.show()

    def inorder(self, bn):
        """中序遍历
        先访问左孩子，再打印根结点，最后访问右孩子
        first, access the left node
        then, access the root node
        finally, access the right node
        left -> mid -> right
        """

        def recursive(bn):
            if bn:
                recursive(bn.left)
                order.append(bn.data)
                recursive(bn.right)

        order = []
        recursive(bn)
        return order

    def postorder(self, bn):
        """后序遍历
        先依次访问左右孩子，再打印根结点
        first, access the left and right node respectively
        then, access the mid node
        left -> right -> mid
        """

        def recursive(bn):
            if bn:
                recursive(bn.left)
                recursive(bn.right)
                order.append(bn.data)

        order = []
        recursive(bn)
        return order

    def preorder(self, bn):
        """前序遍历（深度优先）
        先打印根结点，再依次访问左右孩子
        first, access the mid node
        then, access the left and right node respectively
        mid -> left -> right
        """

        def recursive(bn):
            if bn:
                order.append(bn.data)
                recursive(bn.left)
                recursive(bn.right)

        order = []
        recursive(bn)
        return order

    def levelorder(self, bn):
        """按层遍历（广度优先）
        队列思想，根结点先入队，其附属左右孩子依次入队，最后按出队顺序打印即可
        queue: [m, l, r, ll, rl, lr, rr, lll, ...]
        """

        q = []  # 队列数组
        q.append(bn)  # 根结点入队
        order = []
        while q:  # 队列为非空时
            # 依次出队
            p = q.pop(0)
            order.append(p.data)
            # 附属的左右孩子依次入队
            # 左孩子入队
            if p.left:
                q.append(p.left)
            # 右孩子入队
            if p.right:
                q.append(p.right)

        return order

    def find(self, item):
        """查找某一元素是否存在"""
        for i in self.p:
            if item == i.data:
                return i
        return None

    def update(self, item, change_item):
        """更新一个结点"""
        b = self.find(item)
        if b:
            b.data = change_item
        if item in self.array:
            self.array[self.array.index(item)] = change_item


if __name__ == '__main__':
    item_index = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 13}
    bt = BinaryTree()
    bt.init(item_index)

    print('树的深度为:', bt.depth(bt.mid))
    print('顺序表形式:', bt.array)
    print('广义表形式:', bt.generalized(bt.mid))
    print('树形结构形式:\n', end=bt.tree(bt.mid) + '\n')
    print('前序遍历:', bt.preorder(bt.mid))
    print('中序遍历:', bt.inorder(bt.mid))
    print('后序遍历:', bt.postorder(bt.mid))
    print('按层遍历:', bt.levelorder(bt.mid))
    print('找到的结点:', bt.find('g'))

    bt.draw(bt.mid)

    bt.update('a', 'z')
    print('替换 a 后广义表示：', bt.generalized(bt.mid))

    bt2 = BinaryTree()
    bt2.restore_tree(bt.inorder(bt.mid),
                     pre_order=bt.preorder(bt.mid),
                     post_order=bt.postorder(bt.mid),
                     )
    print('树形结构形式:\n', end=bt2.tree(bt2.mid) + '\n')

"""
init successfully!
树的深度为: 4
顺序表形式: [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', None, None, None, 'j']
广义表形式: a(b(d(h,i),e),c(f(,j),g))
树形结构形式:
a-->b-->d-->h
        └-->i
    └-->e
└-->c-->f
        └-->j
    └-->g
前序遍历: ['a', 'b', 'd', 'h', 'i', 'e', 'c', 'f', 'j', 'g']
中序遍历: ['h', 'd', 'i', 'b', 'e', 'a', 'f', 'j', 'c', 'g']
后序遍历: ['h', 'i', 'd', 'e', 'b', 'j', 'f', 'g', 'c', 'a']
按层遍历: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
找到的结点: g
替换 a 后广义表示： z(b(d(h,i),e),c(f(,j),g))
"""
