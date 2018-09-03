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


class BTree(BLinkList):
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

    def init_order(self):
        self.order = []

    # 初始化树
    def init(self, arr):
        """
        :param arr: list, item index begin at 1, empty item filled with ''
        """
        if arr[0] != 'flag':
            return print('array must be start from the index of 1!')
        if not self.is_empty():
            return print('array is not empty!')
        else:
            self.mid = BNode(arr[1])
            # 二叉链表的存储映象
            # even is left, odd is right, and 1 is mid node
            p = [BNode(None) for _ in range(len(arr))]
            p[1] = self.mid
            for i in range(2, len(arr)):
                if arr[i] == '':
                    continue
                # 左孩子
                if i % 2 == 0:
                    self.lappend(arr[i], p[i // 2])
                    p[i] = p[i // 2].left
                # 右孩子
                else:
                    self.rappend(arr[i], p[i // 2])
                    p[i] = p[i // 2].right
        return print('init successfully!')

    # 打印出二叉树的广义表
    # 根本思想为前序遍历
    def print_(self, bn):
        if bn:
            print(bn.data, end='')  # first
            if bn.left or bn.right:  # then
                # 存在左或右孩子时打印'('
                print('(', end='')
                self.print_(bn.left)
                # 存在右孩子时打印','
                if bn.right:
                    print(',', end='')
                    self.print_(bn.right)
                # 左右孩子都遍历完，打印')'
                print(')', end='')

    # 中序遍历
    # 先访问左孩子，再打印根结点，最后访问右孩子
    def inorder(self, bn):
        """
        first, access the left node
        then, access the root node
        finally, access the right node
        left -> mid -> right
        """
        if bn:
            self.inorder(bn.left)
            self.order.append(bn.data)
            self.inorder(bn.right)

    # 后序遍历
    # 先依次访问左右孩子，再打印根结点
    def postorder(self, bn):
        """
        first, access the left and right node respectively
        then, access the mid node
        left -> right -> mid
        """
        if bn:
            self.postorder(bn.left)
            self.postorder(bn.right)
            self.order.append(bn.data)

    # 前序遍历（深度优先）
    # 先打印根结点，再依次访问左右孩子
    def preorder(self, bn):
        """
        first, access the mid node
        then, access the left and right node respectively
        mid -> left -> right
        """
        if bn:
            self.order.append(bn.data)
            self.preorder(bn.left)
            self.preorder(bn.right)

    # 按层遍历（广度优先）
    # 队列思想，根结点先入队，其附属左右孩子依次入队，最后按出队顺序打印即可
    def levelorder(self, bn):
        """
        queue: [m, l, r, ll, rl, lr, rr, lll, ...]
        """
        q = []  # 队列数组
        q.append(bn)  # 根结点入队
        while len(q) != 0:  # 队列为非空时
            # 依次出队
            p = q.pop(0)
            self.order.append(p.data)
            # 附属的左右孩子依次入队
            # 左孩子入队
            if p.left:
                q.append(p.left)
            # 右孩子入队
            if p.right:
                q.append(p.right)

    # 返回树的深度
    # depth = max(depl, depr)+1
    def depth(self, bn):
        if bn is None:
            return 0
        else:
            depl = self.depth(bn.left)
            depr = self.depth(bn.right)
            if depl > depr:
                return depl + 1
            else:
                return depr + 1

    # 查找某一元素是否存在
    def find(self, item, bn):
        if self.is_empty():
            print('tree is empty!')
            return -1
        if bn.data == item:
            self.bn = bn
            return True
        if bn.left and self.find(item, bn.left):
            return True
        if bn.right and self.find(item, bn.right):
            return True
        return False

    # 获取当前结点
    def get_bn(self):
        return self.bn

    # 更新一个结点
    def update(self, item, change_item, bn):
        self.find(item, bn)
        self.bn.data = change_item


if __name__ == '__main__':
    a = ['' for _ in range(15)]
    item = ['flag', 'a', 'b', 'e', 'c', 'd', 'f', 'g']
    index = [0, 1, 2, 3, 4, 5, 7, 14]
    k = 0
    for i in index:
        a[i] = item[k]
        k += 1
    bt = BTree()
    bt.init(a)
    print('广义表示：', end=' ')
    bt.print_(bt.mid)
    print()

    print('前序遍历:', end=' ')
    bt.init_order()
    bt.preorder(bt.mid)
    print(bt.order)

    print('中序遍历:', end=' ')
    bt.init_order()
    bt.inorder(bt.mid)
    print(bt.order)

    print('后序遍历:', end=' ')
    bt.init_order()
    bt.postorder(bt.mid)
    print(bt.order)

    print('按层遍历:', end=' ')
    bt.init_order()
    bt.levelorder(bt.mid)
    print(bt.order)

    print('树的深度为：', bt.depth(bt.mid))

    bt.find('g', bt.mid)
    bn = bt.get_bn()
    print('找到的结点：', bn)

    bt.update('a', 'z', bt.mid)
    print('替换 a 后广义表示：', end=' ')
    bt.print_(bt.mid)
    print()


"""
init successfully!
广义表示： a(b(c,d),e(,f(g)))
前序遍历: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
中序遍历: ['c', 'b', 'd', 'a', 'e', 'g', 'f']
后序遍历: ['c', 'd', 'b', 'g', 'f', 'e', 'a']
按层遍历: ['a', 'b', 'e', 'c', 'd', 'f', 'g']
树的深度为： 4
找到的结点： g
替换 a 后广义表示： z(b(c,d),e(,f(g)))
"""