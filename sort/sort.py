import math
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter as Writer
import matplotlib.animation as animation
import seaborn as sns

sns.set(style="white", palette="muted", color_codes=True)


class Sort:
    def __init__(self, collect_picture=False):
        self.collect_picture = collect_picture

    def bubble(self, arr, draw_args=dict()):
        """冒泡排序
        相邻元素比较交换，轻者上浮，重者下沉。
        正序时候最快，倒序时候最慢。
        """
        if self.collect_picture:
            self.draw_initialize()

        a = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):

                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

                if self.collect_picture:
                    c = [self.color[0] for _ in range(len(a))]
                    c[j] = self.color[1]
                    c[j + 1] = self.color[1]
                    self.collect_pic(range(len(a)), a, c)

        if self.collect_picture:
            self.show(draw_args)

        return a

    def straight_insert(self, arr, draw_args=dict()):
        """直接插入排序
        每次从无序表中取出第一个元素，把它插入到有序表的合适位置，使有序表仍然有序。
        序列小，基本有序，宜用。
        """
        if self.collect_picture:
            self.draw_initialize()

        a = arr.copy()
        n = len(a)

        for i in range(1, n):
            x = a[i]  # 待插入的数据
            for j in range(i - 1, -1, -1):  # range(3, -1, -1) => (3,2,1,0)
                if x < a[j]:
                    a[j + 1] = a[j]  # 插入数据较小，该位置数据往后挪一位

                    if self.collect_picture:
                        c = [self.color[0] for _ in range(n)]
                        c[j] = self.color[1]
                        c[j + 1] = self.color[1]
                        c[i] = self.color[2]
                        self.collect_pic(range(n), a, c)

                else:
                    j = j + 1  # 插入数据较大，下标返回该数据现在的坐标
                    break

            a[j] = x  # 插入到空出来的位置上

            if self.collect_picture:
                c = [self.color[0] for _ in range(n)]
                if i == j:
                    c[j - 1] = self.color[1]
                else:
                    c[j] = self.color[1]
                c[i] = self.color[2]
                self.collect_pic(range(n), a, c)

        if self.collect_picture:
            self.show(draw_args)

        return a

    def shell(self, arr, step=2, draw_args=dict()):
        """希尔排序
        直接插入排序算法的改进版本。按照步长插入。
        """
        if self.collect_picture:
            self.draw_initialize()

        if step < 2:
            return None

        a = arr.copy()
        n = len(a)
        d = n // step

        while d > 0:
            for i in range(d, n):
                x = a[i]  # 待插入的数据
                for j in range(i - d, -1, -d):
                    if x < a[j]:
                        a[j + d] = a[j]  # 组内比较和移动

                        if self.collect_picture:
                            c = [self.color[0] for _ in range(n)]
                            c[j] = self.color[1]
                            c[j + d] = self.color[1]
                            c[i] = self.color[2]
                            self.collect_pic(range(n), a, c)

                    else:
                        j += d
                        break

                a[j] = x

                if self.collect_picture:
                    c = [self.color[0] for _ in range(n)]
                    if i == j:
                        c[j - d] = self.color[1]
                    else:
                        c[j] = self.color[1]
                    c[i] = self.color[2]
                    self.collect_pic(range(n), a, c)

            d = d // step

        if self.collect_picture:
            self.show(draw_args)

        return a

    def straight_select(self, arr, draw_args=dict()):
        """直接选择排序
        依次选择最小值进行交换。n-1次选择交换后变成有序表。
        """
        if self.collect_picture:
            self.draw_initialize()

        a = arr.copy()
        n = len(a)
        for i in range(1, n):
            k = i - 1  # 保存当前排序区间第一个位置的下标
            for j in range(i, n):  # 当前排序区间中查找最小值的下标
                if self.collect_picture:
                    c = [self.color[0] for _ in range(n)]
                    c[j] = self.color[1]
                    c[k] = self.color[2]
                    self.collect_pic(range(n), a, c)

                if a[j] < a[k]:
                    k = j

            if k != i - 1:
                a[i - 1], a[k] = a[k], a[i - 1]  # 如果排序区间第一个位置的元素不是最小的，则元素交换

                if self.collect_picture:
                    c = [self.color[0] for _ in range(n)]
                    c[i - 1] = self.color[1]
                    c[k] = self.color[1]
                    self.collect_pic(range(n), a, c)

        if self.collect_picture:
            self.show(draw_args)

        return a

    def quick_sort(self, arr, draw_args=dict()):
        """快速排序
        又叫划分排序，最快的排序，气泡排序改进版，比较和交换从两端向中间进行。
        序列大，分布随机，宜用。
        """

        def recursive(a, l, r):
            i = l + 1  # 左区间开始坐标
            j = r  # 右区间开始坐标
            x = a[l]  # 基准元素
            while i <= j:  # stop while left meeting right
                while i <= j and a[i] <= x:  # 左小于基准元素，坐标后移
                    if self.collect_picture:
                        c = [self.color[0] for _ in range(len(a))]
                        c[i] = self.color[1]
                        c[j] = self.color[1]
                        c[l] = self.color[2]
                        self.collect_pic(range(len(a)), a, c)

                    i += 1

                while i <= j and a[j] >= x:  # 右大于基准元素，坐标前移
                    if self.collect_picture:
                        c = [self.color[0] for _ in range(len(a))]
                        c[i] = self.color[1]
                        c[j] = self.color[1]
                        c[l] = self.color[2]
                        self.collect_pic(range(len(a)), a, c)

                    j -= 1

                if i < j:  # i<j时，对换
                    a[i], a[j] = a[j], a[i]

                    if self.collect_picture:
                        c = [self.color[0] for _ in range(len(a))]
                        c[i] = self.color[1]
                        c[j] = self.color[1]
                        c[l] = self.color[2]
                        self.collect_pic(range(len(a)), a, c)

                    i += 1
                    j -= 1

            if l != j:
                a[l], a[j] = a[j], x

                if self.collect_picture:
                    c = [self.color[0] for _ in range(len(a))]
                    c[j] = self.color[1]
                    c[l] = self.color[2]
                    self.collect_pic(range(len(a)), a, c)

            if l < j - 1:
                recursive(a, l, j - 1)

            if r > i:
                recursive(a, j + 1, r)

        if self.collect_picture:
            self.draw_initialize()

        a = arr.copy()
        l, r = 0, len(a) - 1
        recursive(a, l, r)

        if self.collect_picture:
            self.show(draw_args)

        return a

    def merge(self, arr, draw_args=dict()):
        """归并排序
        把两个有序表合并成一个有序表，需要一个序列长度的辅助空间
        序列大，宜用
        """
        if self.collect_picture:
            self.draw_initialize()

        a = arr.copy()
        d = 1
        n = len(a)
        while d < n:
            for i in range(0, n, d * 2):
                l = a[i: i + d]
                r = a[i + d: i + 2 * d]

                if not r:
                    break

                cache = [0] * (len(l) + len(r))
                x, y = 0, 0
                while True:
                    if l[x] < r[y]:
                        cache[x + y] = l[x]
                        x += 1
                    else:
                        cache[x + y] = r[y]
                        y += 1

                    if x == len(l):
                        cache[(x + y):] = r[y:]
                        break
                    if y == len(r):
                        cache[(x + y):] = l[x:]
                        break

                a[i: i + 2 * d] = cache

                if self.collect_picture:
                    c = [self.color[0] for _ in range(len(a))]
                    c[i: i + 2 * d] = self.color[1]
                    self.collect_pic(range(len(a)), a, c)

            d *= 2

        if self.collect_picture:
            self.show(draw_args)

        return a

    def heap(self, arr, draw_args=dict()):
        """堆排序
        把序列构成一个大根堆，再取出根节点以及对堆进行重构。（筛运算和对调）
        待排序的序列很大，可能正序或倒序时，宜用。
        """

        def heap_shift(a, n, i):
            """ 做堆
            筛运算=>小的漏下去，大的留下来，从下标n/2-1（向下取整）开始筛选。
            """
            cache = i
            x = a[i]  # 被筛的结点
            j = 2 * i + 1  # 被筛的结点的左孩子的坐标（初始一定存在）
            while j <= n - 1:  # 不存在左孩子时结束循环
                if j < n - 1 and a[j] < a[j + 1]:
                    j = j + 1  # 存在右孩子且右孩子比左孩子大时，取右孩子

                if x < a[j]:
                    a[i] = a[j]  # 被筛的结点比较小时，下移一层

                    if self.collect_picture:
                        c = [self.color[0] for _ in range(len(a))]
                        c[i] = self.color[1]
                        c[j] = self.color[2]
                        self.collect_pic(range(len(a)), a, c)

                    # 继续往下比较筛选
                    i = j
                    j = 2 * i + 1

                else:
                    break

            a[i] = x

            if self.collect_picture:
                c = [self.color[0] for _ in range(len(a))]
                c[i] = self.color[1]
                c[cache] = self.color[2]
                self.collect_pic(range(len(a)), a, c)

        if self.collect_picture:
            self.draw_initialize()

        a = arr.copy()
        n = len(a)
        for i in range(n // 2 - 1, -1, -1):
            heap_shift(a, n, i)

        for i in range(1, n):
            # 第一个元素和当前堆最后一个元素对调，第一个元素为当前堆最大值
            a[0], a[n - i] = a[n - i], a[0]
            # 筛第一个元素
            heap_shift(a, n - i, 0)

        if self.collect_picture:
            self.show(draw_args)

        return a

    def radix_sort(self, arr, radix=10):
        a = arr.copy()
        k = int(math.ceil(math.log(max(a), radix)))

        for i in range(k):
            bucket = [[] for _ in range(radix)]
            for v in a:
                bucket[v // (radix ** i) % radix].append(v)
            a = [k for j in bucket for k in j]

        return a

    def collect_pic(self, x, y, c):
        self.ims.append(self.ax.bar(x, y, color=c, animated=True))

    def draw_initialize(self):
        self.num_img = 0
        self.color = ['r', 'y', 'b', 'g', 'c', 'm', 'k']
        self.ims = []
        self.fig, self.ax = plt.subplots()
        self.fig.set_tight_layout(True)

    def show(self, draw_args):
        ani = animation.ArtistAnimation(self.fig, self.ims, interval=100,
                                        repeat=True, repeat_delay=1000)

        if draw_args.get('save_ani', None):
            ani.save(draw_args['save_ani'], writer=Writer(fps=10))

        if draw_args.get('show_ani', None):
            plt.show()


if __name__ == '__main__':
    import random

    random.seed(6)
    s = Sort(collect_picture=True)

    a = list(range(1, 21))
    random.shuffle(a)

    # s.bubble(a,
    #          draw_args={
    #              'show_ani': False,
    #              'save_ani': 'img/bubble.mp4',
    #          }
    #          )

    # s.straight_insert(a,
    #                   draw_args={
    #                       'show_ani': False,
    #                       'save_ani': 'img/straight_insert.mp4',
    #                   })
    #
    # s.shell(a, 2,
    #         draw_args={
    #             'show_ani': False,
    #             'save_ani': 'img/shell.mp4',
    #         })
    #
    # s.straight_select(a,
    #                   draw_args={
    #                       'show_ani': False,
    #                       'save_ani': 'img/straight_select.mp4',
    #                   })
    #
    # s.quick_sort(a,
    #              draw_args={
    #                  'show_ani': False,
    #                  'save_ani': 'img/quick_sort.mp4',
    #              })
    #
    # s.merge(a,
    #         draw_args={
    #             # 'show_ani': False,
    #             # 'save_ani': 'img/merge.mp4',
    #         }
    #         )
    #
    # s.heap(a,
    #        draw_args={
    #            'show_ani': False,
    #            'save_ani': 'img/heap.mp4',
    #        })
    #
    print(s.radix_sort(a))
