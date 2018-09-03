"""快速排序
又叫划分排序，最快的排序，气泡排序改进版，比较和交换从两端向中间进行。
序列大，分布随机，宜用。
"""


def quick_sort(a, l, r):
    i = l + 1  # 左区间开始坐标
    j = r  # 右区间开始坐标
    x = a[l]  # 基准元素
    while i <= j:   # stop while left meeting right
        while i <= j and a[i] <= x:  # 左小于基准元素，坐标后移
            i += 1
        while i <= j and a[j] >= x:  # 右大于基准元素，坐标前移
            j -= 1
        if i < j:  # i<j时，对换
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if l != j:
        a[l], a[j] = a[j], x
    # 递归
    if l < j - 1:
        quick_sort(a, l, j - 1)
    if r > i:
        quick_sort(a, j + 1, r)


if __name__ == '__main__':
    a = [45, 53, 18, 36, 72, 30, 48, 93, 15, 36]
    n = len(a)
    quick_sort(a, 0, n - 1)
    print(a)

"""
[15, 18, 30, 36, 36, 45, 48, 53, 72, 93]
"""
