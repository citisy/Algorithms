"""希尔排序
直接插入排序算法的改进版本。按照步长插入。
"""


def shell(a):
    n = len(a)
    d = n // 3  # 整除，步长为3
    while d > 0:
        for i in range(d, n):
            x = a[i]  # 待插入的数据
            for j in range(i - d, -1, -d):
                if x < a[j]:
                    a[j + d] = a[j]  # 组内比较和移动
                else:
                    j += d
                    break
            a[j] = x
        d = d // 2  # 缩小步长


if __name__ == '__main__':
    a = [36, 25, 48, 12, 65, 25, 43, 58, 76, 32]
    shell(a)
    print(a)
"""
[12, 25, 25, 32, 36, 43, 48, 58, 65, 76]
"""
