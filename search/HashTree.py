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
        self.mid = Node(0)
        self.creat_tree()

    def creat_tree(self):
        """
        there, we define h(x) = x % p (where p is prime numbers) as the hash function
        the tree's depth is 5, so we can fill 2*3*5*7 numbers
        :return:
        """
        self.p_list = [2, 3, 5, 7]
        bn_list = [self.mid]
        for i, p in enumerate(self.p_list):
            l = []
            for bn in bn_list:
                bn.children = [Node(0) for _ in range(p)]
                l += bn.children
            bn_list = l

    def init(self, arr):
        for a in arr:
            bn = self.mid
            for p in self.p_list:
                x = a % p   # which node will be gone to
                a = a // p
                bn = bn.children[x]
                if a == 0:  # when a is 0, it can't go down
                    bn.data = 1
                    break

    def search(self, item):
        bn = self.mid
        for p in self.p_list:
            x = item % p
            item = item // p
            bn = bn.children[x]
            if item == 0:
                if bn.data == 1:
                    return True
                else:
                    return False


if __name__ == '__main__':
    a = [45, 36, 18, 53, 72, 30, 48, 93, 15, 36]
    h = HTree()
    h.init(a)

    print(h.search(72))
    print(h.search(73))

"""
True
False
"""