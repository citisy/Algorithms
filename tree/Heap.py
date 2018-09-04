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
        self.h = [BNode(None)]  # 堆的存储映象

    def init(self, arr):
        for i in arr:
            self.insert(i)

    # 插入一个叶子结点
    def insert(self, item):
        # 堆为空，作为根结点插入
        if self.is_empty():
            self.mid = BNode(item)
            self.h.append(self.mid)
        # 非空
        else:
            # 找出堆尾
            n = len(self.h)
            # 把元素插到堆尾
            newp = BNode(item)
            if n % 2 == 0:
                self.h[n // 2].left = newp
            else:
                self.h[n // 2].right = newp
            self.h.append(newp)
            # compared with the parent, if the item is small, swap them, then, repeat the action
            while n != 1 and item < self.h[n // 2].data:
                self.h[n].data, self.h[n // 2].data = self.h[n // 2].data, self.h[n].data
                n = n // 2

    # 删除堆顶结点，并返回堆顶元素
    def delete(self):
        n = len(self.h) - 1  # index 0 of h is None, so h's real len must sub 1
        if n == 0:   # heap is empty
            return None
        # 非空
        else:
            bn_data = self.mid.data  # return data
            self.mid.data = self.h.pop().data   # tail of heap move to head
            # 比较下移
            n -= 1
            i = 1
            # h => 存储较小的孩子
            # 如果有右结点，两者比较
            if i <= n and self.h[i].right:
                if self.h[i].left.data < self.h[i].right.data:
                    h = self.h[i].left
                else:
                    h = self.h[i].right
            # 只有左结点
            elif i <= n and self.h[i].left:
                h = self.h[i].left
            # 不是叶子结点，且值较大
            while i * 2 <= n and self.h[i] and self.h[i].data > h.data:
                self.h[i].data, h.data = h.data, self.h[i].data
                # 如果有右结点，两者比较
                if self.h[i].right:
                    if self.h[i].left.data < self.h[i].right.data:
                        h = self.h[i].left
                    else:
                        h = self.h[i].right
                # 只有左结点
                elif self.h[i].left:
                    h = self.h[i].left
                i *= 2
            return bn_data


if __name__ == '__main__':
    arr = [73, 26, 48, 18, 60, 35, 50]
    bt = Heap()
    bt.init(arr)

    print('广义表:', end=' ')
    bt.print_(bt.mid)
    print()

    while 1:
        bn_data = bt.delete()
        if bn_data is None:
            break
        print(bn_data, end=' ')

"""
广义表: 18(26(73,60),35(48,50))
18 26 35 48 50 60 73
"""