"""堆，一颗完全二叉树，宜采用顺序存储，这里使用链式存储
基本特征：小根堆：根<左孩子or右孩子，大根堆：根>左孩子or右孩子
"""

from tree.BinaryTree import *


# 小根堆
class Heap(BTree):
    """
    functions:
        insert(item, bn): insert an item
        delete(item, bn): delete an item
    """

    def __init__(self):
        super(Heap, self).__init__()

    def init(self, arr):
        for i in arr:
            self.insert(i)

    # 插入一个叶子结点
    def insert(self, item):
        # 堆为空，作为根结点插入
        if self.is_empty():
            self.p.append(BNode(None))
            self.p.append(BNode(item))
        # 非空
        else:
            n = len(self.p)
            # 把元素插到堆尾
            self.p.append(BNode(item))
            # compared with the parent, if the item is small, swap them, then, repeat the action
            while n != 1 and item < self.p[n // 2].data:
                self.p[n].data, self.p[n // 2].data = self.p[n // 2].data, self.p[n].data
                n = n // 2
        self.mid = self.get_mid(self.p)

    # 删除堆顶结点，并返回堆顶元素
    def delete(self):
        n = len(self.p) - 1  # index 0 of h is None, so h's real len must sub 1
        if n == 0:      # heap is empty
            bn_data = None
        elif n == 1:    # only have mid node
            bn_data = self.p.pop().data
            self.mid = None
        else:
            bn_data = self.p[1].data
            if n % 2 == 0:  # cut the line of parent to children
                self.p[n // 2].left = None
            else:
                self.p[n // 2].right = None
            self.p[1].data = self.p.pop().data  # tail of heap move to head
            i = 1
            while i < n and self.p[i]:
                if i * 2 + 1 < n:  # have right children
                    if self.p[i * 2].data < self.p[i * 2 + 1].data:
                        p = self.p[i * 2]
                        j = i * 2
                    else:
                        p = self.p[i * 2 + 1]
                        j = i * 2 + 1
                elif i * 2 < n:  # have left children
                    p = self.p[i * 2]
                    j = i * 2
                else:
                    break
                if self.p[i].data > p.data:
                    self.p[i].data, p.data = p.data, self.p[i].data
                i = j
            self.mid = self.get_mid(self.p)
        return bn_data


if __name__ == '__main__':
    import random

    arr = list(range(1, 11))
    random.shuffle(arr)

    bt = Heap()
    bt.init(arr)

    print('广义表:', end=' ')
    bt.print_(bt.mid)
    print()

    print('树状结构：')
    bt.show(bt.mid)
    print()

    print('get data:', end=' ')
    while 1:
        bn_data = bt.delete()
        if bn_data is None:
            break
        print(bn_data, end=' ')

"""
广义表: 1(2(5(10,8),4(9)),3(6,7))
树状结构：
1 -- 2 -- 5 -- 10
            |- 8
       |- 4 -- 9
  |- 3 -- 6
       |- 7
get data: 1 2 3 4 5 6 7 8 9 10 
"""
