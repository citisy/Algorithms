# -*- coding: utf-8 -*-

# 直接选择排序
# 依次选择最小值进行交换。n-1次选择交换后变成有序表。
# test data: 36 25 48 12 65 25 43 58 76 32
# output: [12, 25, 25, 32, 36, 43, 48, 58, 65, 76]

a = input()
a = a.split(' ')
a = [int(i) for i in a]
n = len(a)

for i in range(1, n):
    k = i - 1  # 保存当前排序区间第一个位置的下标
    for j in range(i, n):  # 当前排序区间中查找最小值的下标
        if a[j] < a[k]:
            k = j
    if k != i - 1:
        a[i-1], a[k] = a[k], a[i-1]  # 如果排序区间第一个位置的元素不是最小的，则元素交换
print(a)