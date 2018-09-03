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


    def __repr__(self):
        """
        print(Node)
            >> data
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
        self.mid = None  # middle node or root node

    # 链表是否为空
    def is_empty(self):
        return self.mid is None

    # 初始化
    def init(self, arr):
        pass

    # 链表长度
    def lenth(self):
        pass

    # 当前结点的右指针添加一个结点
    def rappend(self, item, bn):
        # 链表为空
        if self.is_empty():
            self.mid = BNode(item)
        else:
            newp = BNode(item)
            bn.right = newp

    # 左指针添加一个结点
    def lappend(self, item, bn):
        # 链表为空
        if self.is_empty():
            self.mid = BNode(item)
        else:
            newp = BNode(item)
            bn.left = newp

    # 清空链表
    def clear(self):
        self.mid = None