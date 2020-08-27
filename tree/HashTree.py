"""哈希树
特点：
1.哈希树的结构是动态的，也不像某些哈希算法那样需要长时间的初始化过程，只需要初始化根结点就可以开始工作。哈希树也没 有必要为不存在的关键字提前分配空间。
2.查找迅速，最多只需要10次取余和比较操作，就可知道这个对象是否存在。哈希树的查找次数和元素个数没有关系。
3.结构不变，哈希树在删除的时候并不做任何结构调整。这也是它的一个非常好的优点。常规树结构在增加元素和删除元素的时候都要做一定的结构调整。
4.非排序性，哈希树不支持排序，没有顺序特性。
需要注意的是：哈希树是一个单向增加的结构，即随着所需要存储的数据量增加而增大。即使数据量减少到原来的数量，但是哈希树的总结点树不会减少。这样做的目的是为了避免结构的调整带来的额外消耗。
用空间换取时间，创建哈希树会耗时较长，其性能由哈希函数决定
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


class HTree:
    def __init__(self):
        self.mid = Node(None)
        self.primes = [2, 3, 5, 7, 11, 13, 19, 23, 29]

    def init(self, arr):
        for a in arr:
            self.insert(a)

    def insert(self, item):
        item = item if isinstance(item, int) else ord(item)
        bn = self.mid
        p = Node(item)
        for prime in self.primes:
            mod = item % prime

            if not bn.children:
                bn.children = [None for _ in range(prime)]

            if not bn.children[mod]:
                bn.children[mod] = p
                break

            if bn.children[mod].data is None:
                bn.children[mod].data = item
                break

            bn = bn.children[mod]

    def search(self, item):
        item = item if isinstance(item, int) else ord(item)
        bn = self.mid

        for prime in self.primes:
            mod = item % prime

            if not bn.children:
                return False

            if not bn.children[mod]:
                return False

            elif bn.children[mod].data == item:
                return bn

            else:
                bn = bn.children[mod]

    def delete(self, item):
        bn = self.search(item)
        if bn:
            bn.data = None
            return True


if __name__ == '__main__':
    a = [45, 36, 18, 53, 72, 30, 48, 93, 15, 36]
    h = HTree()
    h.init(a)

    print(h.search(72))
    print(h.search(73))

    print(h.delete(45))
    for i in a:
        print(h.search(i))

"""
True
False
"""
