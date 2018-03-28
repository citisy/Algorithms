# -*- coding: utf-8 -*-

# 堆，一颗完全二叉树，宜采用顺序存储，这里使用链式存储
# 基本特征：小根堆：根<左孩子or右孩子，大根堆：根>左孩子or右孩子

import sys
sys.path.append('../link_list')
from BLinkList import BNode
from BTree import BTree


# 小根堆
class Heap(BTree):
    '''
    inserst(item, bn): 插入一个叶子结点
    delete(item, bn): 删除一个结点
    '''

    def __init__(self):
        super(Heap, self).__init__()
        self.h = [BNode('')]  # 堆的存储映象

    # 重写父类方法
    def init(self, arr):
        super().init(arr)
        self.__creat_h()

    # 按层遍历初始化堆的存储映象
    def __creat_h(self):
        front = 0  # 队首指针
        rear = 0  # 队尾指针
        maxsize = 30  # 队列的数组长度
        q = ['' for _ in range(maxsize)]  # 队列数组
        # 根结点入队
        if self.mid and self.mid.data != '':
            rear = (rear + 1) % maxsize
            q[rear] = self.mid
        # 队列为非空时
        while front != rear:
            front = (front + 1) % maxsize
            # 依次出队
            p = q[front]
            self.h.append(p)
            # 附属的左右孩子依次入队
            # 左孩子入队
            if p.left and p.left.data != '':
                rear = (rear + 1) % maxsize
                q[rear] = p.left
            # 右孩子入队
            if p.right and p.right.data != '':
                rear = (rear + 1) % maxsize
                q[rear] = p.right

    # 插入一个叶子结点
    def inserst(self, item):
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
            # 较小，与双亲结点互换位置
            while n != 1 and item < self.h[n // 2].data:
                self.h[n].data, self.h[n // 2].data = self.h[n // 2].data, self.h[n].data
                n = n // 2

    # 删除堆顶结点，并返回堆顶元素
    def delete(self):
        n = len(self.h) - 1
        # 堆为空
        if n == 0:
            return 'heap is empty!', False
        # 非空
        else:
            # 弹出堆顶元素
            bn = self.mid.data
            # 堆尾元素移到堆顶
            if n > 0:
                self.mid.data = self.h[-1].data
                self.h[-1] = None
                self.h.pop()
            # 比较下移
            n = len(self.h) - 1
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
            while i*2 <= n and self.h[i] and self.h[i].data > h.data:
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
            return bn, True

if __name__ == '__main__':
    arr = [73, 26, 48, 18, 60, 35, 50]
    bt = Heap()
    for i in arr:
        bt.inserst(i)
    print('广义表:', end=' ')
    bt.print_(bt.mid)
    print()
    bn, flag = bt.delete()
    print(bn, end=' ')
    while flag:
        bn, flag = bt.delete()
        print(bn, end=' ')
