# -*- coding: utf-8 -*-

from ALinkList import Node
from ALinkList import LinkList


# 用单链表实现多项式求和：p=a0+a1x^1+...+anx^n
# 每个结点有两个域，第一个保存系数，第二个保存指数
def polysum(l, x):
    p = l.head
    y = 0
    while p:
        y += p.data[0] * x ** p.data[1]
        p = p.next
    return y


# 用单链表实现两个多项式相加=>p1+p2
# 每个结点有两个域，第一个保存系数，第二个保存指数
def polyadd(l1, l2):
    p1 = l1.head
    p2 = l2.head
    p = LinkList()
    while p1 and p2:
        # 指数相等，系数相加
        if p1.data[1] == p2.data[1]:
            p.append([p1.data[0]+p2.data[0], p2.data[1]])
            p1 = p1.next
            p2 = p2.next
        # 保存指数较小的项
        elif p1.data[1] > p2.data[1]:
            p.append([p2.data[0], p2.data[1]])
            p2 = p2.next
        else:
            p.append([p1.data[0], p1.data[1]])
            p1 = p1.next
    # 保存p1或p2剩下的项
    while p1:
        p.append([p1.data[0], p1.data[1]])
        p1 = p1.next
    while p2:
        p.append([p2.data[0], p2.data[1]])
        p2 = p2.next
    return p


if __name__ == '__main__':
    # test polysum
    data1 = [[5, 0], [3, 2], [-6, 3], [2, 5]]
    l1 = LinkList()
    l1.init(data1)
    x = 2
    y = polysum(l1, x)
    print(y)
    # test polyadd
    data2 = [[3, 0], [4, 1], [-2, 2], [3, 3], [-2, 5], [9, 6]]
    l2 = LinkList()
    l2.init(data2)
    l = polyadd(l1, l2)
    l.traverse()
