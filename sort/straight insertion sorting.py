# -*- coding: utf-8 -*-

# 直接插入排序
# 每次从无序表中取出第一个元素，把它插入到有序表的合适位置，使有序表仍然有序。
# 序列小，基本有序，宜用。
# test data: 42 65 80 74 28 44 36 65
# output: [28, 36, 42, 44, 65, 65, 74, 80]
a = input()
a = a.split(' ')
a = [int(i) for i in a]
n = len(a)

for i in range(1, n):
    x = a[i]  # 待插入的数据
    for j in range(i-1, -1, -1):  # range(3, -1, -1)=>(3,2,1,0)
        if x < a[j]:
            a[j+1] = a[j]  # 插入数据较小，该位置数据往后挪一位
        else:
            j = j+1  # 插入数据较大，下标返回该数据现在的坐标
            break
    a[j] = x  # 插入到空出来的位置上

print(a)