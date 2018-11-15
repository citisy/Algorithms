"""气泡排序
相邻元素比较交换，轻者上浮，重者下沉。
正序时候最快，倒序时候最慢。
"""
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", palette="muted", color_codes=True)
import imageio
import os

def bubble(a):
    global z
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            c = ['r' for _ in range(10)]
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            c[j] = 'y'
            c[j + 1] = 'y'
            show(range(10), a, c)

    for i in range(z):
        frames.append(imageio.imread('cache/%d.png' % i))
    imageio.mimsave('img/bs.gif', frames, 'GIF', duration=0.25)
    for i in range(z):
        os.remove('cache/%d.png' % i)

frames = []
z = 0


def show(x, y, c):
    global z
    plt.clf()
    plt.bar(x, y, color=c)  # todo: bar can't use animation method, finding a better way to save the gif, ing...
    plt.savefig('cache/%d.png' % z)
    z += 1
    plt.draw()
    plt.pause(0.01)


if __name__ == '__main__':
    import random

    a = list(range(1, 11))
    random.shuffle(a)
    bubble(a)
    print(a)

"""
[12, 25, 25, 32, 36, 43, 48, 58, 65, 76]
"""
