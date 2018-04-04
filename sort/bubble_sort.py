# -*- coding: utf-8 -*-

# 气泡排序
# 相邻元素比较交换，轻者上浮，重者下沉。
# 正序时候最快，倒序时候最慢。
# test data: 36 25 48 12 65 25 43 58 76 32
# output: [12, 25, 25, 32, 36, 43, 48, 58, 65, 76]

a = input()
a = a.split(' ')
a = [int(i) for i in a]
n = len(a)

# 从后往前
for i in range(n):
    for j in range(n-1, i-1, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
print(a)