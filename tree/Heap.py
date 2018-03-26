# -*- coding: utf-8 -*-

# 堆
# 基本特征：小根堆：根<左孩子<右孩子，大根堆：根>左孩子>右孩子

from BTree import BTree


class Heap(BTree):
    '''
    inserst(item, bn): 插入一个结点
    delete(item, bn): 删除一个结点
    '''

    # 初始化
    def init(self, arr):
        super().init(arr)

    # 插入一个结点
    def inserst(self, item, bn):
        pass

    # 删除一个结点
    def delete(self, item, bn):
        pass

if __name__ == '__main__':
    a = ['' for _ in range(15)]
    item = ['flag', 'a', 'b', 'e', 'c', 'd', 'f', 'g']
    index = [0, 1, 2, 3, 4, 5, 7, 14]
    k = 0
    for i in index:
        a[i] = item[k]
        k += 1
    bt = Heap()
    bt.init(a)
    print('广义表示：', end=' ')
    bt.print_(bt.mid)
    print()