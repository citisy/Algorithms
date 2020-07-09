"""创建一个保存data和左右指针的的对象，模拟二叉链表
这是一个基类文件，这里只是简单定义了一些方法，主要服务于后面的二叉树"""


class BNode:
    def __init__(self, data, left=None, right=None):
        """
        data: 数据域
        next: 结点指针
        """
        self.data = data
        self.left = left
        self.right = right
        # self.parent = None  # unnecessary, but easy to find the parent

    def __repr__(self):
        return str(self.data)


class BLinkList:
    """
    functions：
        is_empty(): 判断是否为空
        init(): 初始化
        length(): 返回链表长度
        rappend(item): 链表右结尾添加一个结点
        lappend(item): 链表左结尾添加一个结点
        clear(): 清空单链表
    """

    def __init__(self):
        self.mid = None  # tree like structure
        self.array = []  # array like structure
        self.p = []  # store node list

    def is_empty(self):
        """judge weather the LinkList is empty or not"""
        return self.mid is None

    def length(self):
        """
        :return: length of LinkList
        """
        pass

    def init(self, dic: dict):
        """initial the LinkList
        :param dic: dict type, {item: site}
        eg:
            if a BLinkList tree like this:
                    1
                  / \
                2   3
               /\    \
              4 5    7
            the dic is {'1':1, '2':2, '3':3, '4':4, '5':5, '7':7}
        """
        pass

    def rappend(self, item, bn):
        """
        :param item: which item want to append
        :param bn: which node's right child want to append
        """
        if self.is_empty():
            self.mid = BNode(item)
        else:
            newp = BNode(item)
            bn.right = newp

    def lappend(self, item, bn):
        """
        :param item: which item want to append
        :param bn: which node's left child want to append
        """
        if self.is_empty():
            self.mid = BNode(item)
        else:
            newp = BNode(item)
            bn.left = newp

    def get_mid(self, p):
        """
        get a tree like structure
        :param p: store node list
        :return: mid
        """
        for i in range(1, len(p) // 2 + 1):
            if 2 * i < len(p) and p[2 * i].data is not None:
                p[i].left = p[2 * i]
            if 2 * i + 1 < len(p) and p[2 * i + 1].data is not None:
                p[i].right = p[2 * i + 1]

        return p[1]

    def get_array(self, bn):
        """
        get a array like structure
        :param p: store node list
        :return: array
        """
        q = []  # 队列数组
        q.append(bn)  # 根结点入队
        array = [None]
        while q:  # 队列为非空时
            # 依次出队
            p = q.pop(0)
            if p:
                array.append(p.data)
                q.append(p.left if p.left else None)
                q.append(p.right if p.right else None)
            else:
                array.append(None)

        return array

    def clear(self):
        """clear the LinkList"""
        self.mid = None
