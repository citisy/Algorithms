"""堆，一颗完全二叉树，宜采用顺序存储，这里使用链式存储
基本特征：小根堆：根<左孩子or右孩子，大根堆：根>左孩子or右孩子
"""

from BinaryTree import BinaryTree


# 小根堆
class Heap(BinaryTree):
    """
    functions:
        insert(item, bn): insert an item
        delete(item, bn): delete an item
    """

    def init(self, arr):
        for i in arr:
            self.insert(i)

    def insert(self, item):
        """插入一个叶子结点"""

        # 堆为空，作为根结点插入
        if self.is_empty():
            if not self.p:
                self.p.append(self.node(None))
            self.p.append(self.node(item))
        # 非空
        else:
            n = len(self.p)
            # 把元素插到堆尾
            self.p.append(self.node(item))
            # compared with the parent, if the item is small, swap them, then, repeat the action
            while n != 1 and item < self.p[n // 2].data:
                self.p[n].data, self.p[n // 2].data = self.p[n // 2].data, self.p[n].data
                n = n // 2
        self.mid = self.get_mid(self.p)

    def get_data(self):
        """删除堆顶结点，并返回堆顶元素"""

        n = len(self.p) - 1  # index 0 of tree is None, so tree's real length must sub 1
        if n == 0:  # heap is empty
            bn_data = None
        elif n == 1:  # only have mid node
            bn_data = self.p.pop().data
            self.mid = None
        else:
            bn_data = self.p[1].data
            if n % 2 == 0:  # delete the tail of heap
                self.p[n // 2].left = None
            else:
                self.p[n // 2].right = None

            self.p[1].data = self.p.pop().data  # tail of heap move to head
            i = 1
            while i < n and self.p[i]:
                if i * 2 + 1 < n:  # have right children
                    if self.p[i * 2].data < self.p[i * 2 + 1].data:     # 左孩子的值小于右孩子的值，取左孩子
                        p = self.p[i * 2]
                        j = i * 2
                    else:   # 否则取右孩子
                        p = self.p[i * 2 + 1]
                        j = i * 2 + 1
                elif i * 2 < n:  # have left children
                    p = self.p[i * 2]   # 因为没有右孩子了，所以只需要跟左孩子比较就可以了。
                    j = i * 2
                else:
                    break

                if self.p[i].data > p.data:
                    self.p[i].data, p.data = p.data, self.p[i].data
                else:
                    break

                i = j

            self.mid = self.get_mid(self.p)

        return bn_data


if __name__ == '__main__':
    import random

    random.seed(0)

    arr = list(range(1, 11))
    random.shuffle(arr)
    print("输入序列:", arr)

    bt = Heap()
    bt.init(arr)
    # bt.draw(bt.mid)
    print('广义表形式:', bt.generalized(bt.mid))
    print('树形结构形式:\n', end=bt.tree(bt.mid) + '\n')

    print('从小到大出队:', end=' ')
    while 1:
        bn_data = bt.get_data()
        if bn_data is None:
            break
        print(bn_data, end=' ')

"""
输入序列: [8, 9, 2, 6, 4, 5, 3, 1, 10, 7]
广义表形式: 1(2(4(9,10),6(7)),3(8,5))
树形结构形式:
1-->2-->4-->9
        └-->10
    └-->6-->7
└-->3-->8
    └-->5
从小到大出队: 1 2 3 4 5 6 7 8 9 10
"""
