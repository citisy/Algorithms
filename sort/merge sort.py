# -*- coding: utf-8 -*-

# 归并排序
# 把两个有序表合并成一个有序表，需要一个序列长度的辅助空间
# 序列大，宜用
# test data: 45 53 18 36 72 30 48 93 15 36
# output: [15, 18, 30, 36, 36, 45, 48, 53, 72, 93]

a = input()
a = a.split(' ')
a = [int(i) for i in a]
n = len(a)

# 二路归并
def merge(l, r):
    res = []
    while l and r:  # left和right都不为空时
        # 按大小排序
        if l[0] < r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
    while l:
        res.append(l.pop(0))
    while r:
        res.append(r.pop(0))
    return res

def merge_sort(arr):
    n = len(arr)
    if n < 2:  # arr只有1个元素时，返回原数列
        return arr
    m = n // 2  # 取数列中心点坐标
    l, r = arr[:m], arr[m:]  # 左右序列
    # 递归
    return merge(merge_sort(l), merge_sort(r))

print(merge_sort(a))