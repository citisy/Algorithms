"""堆排序
把序列构成一个大根堆，再取出根节点以及对堆进行重构。（筛运算和对调）
待排序的序列很大，可能正序或倒序时，宜用。
"""


class heap:
    def __init__(self, a):
        self.a = a
        self.n = len(self.a)

    # 建立初始堆
    def init(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.shift(a, self.n, i)

    def sort(self):
        # 排序
        for i in range(1, self.n):
            # 第一个元素和当前堆最后一个元素对调，第一个元素为当前堆最大值
            a[0], a[self.n - i] = a[self.n - i], a[0]
            # 筛第一个元素
            self.shift(a, self.n - i, 0)

    # 做堆
    # 筛运算=>小的漏下去，大的留下来，从下标n/2-1（向下取整）开始筛选。
    def shift(self, a, n, i):
        x = a[i]  # 被筛的结点
        j = 2 * i + 1  # 被筛的结点的左孩子的坐标（初始一定存在）
        while j <= n - 1:  # 不存在左孩子时结束循环
            if j < n - 1 and a[j] < a[j + 1]:
                j = j + 1  # 存在右孩子且右孩子比左孩子大时，取右孩子
            if x < a[j]:
                a[i] = a[j]  # 被筛的结点比较小时，下移一层
                # 继续往下比较筛选
                i = j
                j = 2 * i + 1
            else:
                break
        a[i] = x


if __name__ == '__main__':
    a = [45, 36, 18, 53, 72, 30, 48, 93, 15, 36]
    h = heap(a)
    h.init()
    h.sort()
    print(a)

"""
[15, 18, 30, 36, 36, 45, 48, 53, 72, 93]
"""
