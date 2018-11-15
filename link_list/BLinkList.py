"""创建一个保存data和左右指针的的对象，模拟二叉链表"""


class BNode(object):
    def __init__(self, data):
        """
        data: 数据域
        next: 结点指针
        """
        self.data = data
        self.left = None
        self.right = None
        # self.parent = None  # unnecessary, but easy to find the parent

    def __repr__(self):
        """
        >>> print(Node)
        >>> data
        """
        return str(self.data)


class BLinkList(object):
    """
    functions：
        is_empty(): 判断是否为空
        init(): 初始化
        lenth(): 返回链表长度
        rappend(item): 链表右结尾添加一个结点
        lappend(item): 链表左结尾添加一个结点
        clear(): 清空单链表
    """

    def __init__(self):
        self.mid = None  # tree like structure
        self.array = []    # array like structure
        self.p = []     # store node list
        self.order = []  # traverse order

    def is_empty(self):
        """
        judge weather the linklist is empty or not
        """
        return self.mid is None

    def init(self, dic):
        """
        initial the linklist
        :param dic: dict type, if a Blinklist tree like this:
                1
              / \
            2   3
           /\    \
          4 5    7
        the dic is {'1':1, '2':2, '3':3, '4':4, '5':5, '7':7}
        """
        pass

    def lenth(self):
        """
        :return: length of linklist
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

    def clear(self):
        """
        clear the linklist
        """
        self.mid = None

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

    def get_array(self, p):
        """
        get a array like structure
        :param p: store node list
        :return: array
        """
        return [_.data for _ in p]
