"""归并排序
把两个有序表合并成一个有序表，需要一个序列长度的辅助空间
序列大，宜用
"""


# 二路归并
def merge(l, r):
    ret = []    # save the result of each sort
    while l and r:  # left和right都不为空时
        # 按大小排序
        if l[0] < r[0]:
            ret.append(l.pop(0))
        else:
            ret.append(r.pop(0))
    while l:    # right is already empty
        ret.append(l.pop(0))
    while r:    # left is already empty
        ret.append(r.pop(0))
    return ret


def merge_sort(arr):
    n = len(arr)
    if n < 2:  # arr has only one item or is empty
        return arr
    m = n // 2  # 取数列中心点坐标
    l, r = arr[:m], arr[m:]  # 左右序列
    # 递归
    return merge(merge_sort(l), merge_sort(r))


if __name__ == '__main__':
    a = [45, 53, 18, 36, 72, 30, 48, 93, 15, 36]
    print(merge_sort(a))

"""
[15, 18, 30, 36, 36, 45, 48, 53, 72, 93]
"""