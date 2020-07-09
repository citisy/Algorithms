"""创建一个保存data和next的对象，模拟单链表"""


class Node:
    def __init__(self, data, next=None):
        """
        data: 数据域
        next: 结点指针
        """
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class LinkList:
    """
    functions：
        is_empty(): 判断是否为空
        init(data): 初始化单链表
        length(): 返回单链表长度
        get(pos): 取第pos个元素
        traverse(): 遍历单链表并打印
        find(item): 查找单链表某值的位置
        update(pos, item): 更新第pos个结点
        insert(pos, item): 在pos位置后插入元素
        append(item): 单链表结尾添加一个元素
        sort(): 对单链表进行排序
        delete(pos): 删除第pos个元素
        clear(): 清空单链表
    """

    def __init__(self):
        self.head = None  # head node

    def is_empty(self) -> bool:
        """判断是否为空"""
        return self.head is None

    def length(self) -> int:
        """返回单链表长度"""
        if self.is_empty():
            print('LinkList is empty')
            return -1
        i = 1
        p = self.head
        while p.next:
            i += 1
            p = p.next
        return i

    def is_pos(self, pos) -> bool:
        """判断pos是否符合要求"""
        if pos < 0:
            print('error: pos must be greater than 0!')
            return False
        elif pos > self.length() - 1:
            print('error: pos must be smaller than LinkList\'s length!')
            return False

        return True

    def init(self, data: list) -> None:
        """初始化单链表"""
        data = data.copy()

        if self.is_empty():
            self.head = Node(data.pop(0))  # init head node as data[0]

        p = self.head

        for i in data:  # traverse the data and made it become node's next
            p.next = Node(i)
            p = p.next

        print('init successfully!')

    def append(self, item: object) -> None:
        """单链表结尾添加一个元素"""
        # 链表为空
        if self.is_empty():
            self.head = Node(item)
        else:
            p = self.head

            while p.next:
                p = p.next

            p.next = Node(item)

    def insert(self, pos=0, item=None) -> int:
        """在pos位置后插入元素"""

        if not self.is_pos(pos):
            return -1

        d = Node(None, self.head)
        i = 0
        p = d

        while p.next and i != pos:
            p = p.next
            i += 1

        newp = Node(item, p.next)  # 插入元素创建新结点
        p.next = newp
        self.head = d.next
        print('insert successfully!')
        return pos

    def update(self, pos=0, item=None) -> int:
        """更新第pos个结点"""

        if not self.is_pos(pos):
            return -1

        i = 0
        p = self.head
        while p and i != pos:
            i += 1
            p = p.next

        p.data = item
        print('update successfully!')
        return pos

    def sort(self) -> bool:
        """对单链表进行排序
        使用直接插入排序，从小到大排序"""
        if self.is_empty() or self.length() == 1:
            return False

        xp = self.head
        cp = xp.next  # 待比较元素
        while cp:
            p = self.head
            q = None
            while p is not cp and p.data < cp.data:  # 依次往后比较
                q = p
                p = p.next

            if p is cp:
                xp = cp  # 待比较元素较大，后移一位
            else:
                xp.next = cp.next  # 弹出cp结点

                # 待比较元素插入到q后面
                cp.next = p  # cp指针指向p

                # q指针指向cp
                if q is None:
                    self.head = cp
                else:
                    q.next = cp

            cp = xp.next

        print('sort successfully!')
        return True

    def traverse(self) -> str:
        """遍历单链表并打印"""
        p = self.head
        s = ''
        while p:
            s += str(p.data) + ' -> '
            p = p.next

        return s + 'null'

    def find(self, item: object) -> int:
        """查找单链表某值的位置"""
        p = self.head
        pos = 1
        while p:
            if item == p.data:
                return pos
            pos += 1
        print('not found!')
        return -1

    def get(self, pos=0) -> object:
        """取第pos个元素"""
        if not self.is_pos(pos):
            return -1

        i = 0
        p = self.head
        while p:
            if i == pos:
                return p.data
            p = p.next
            i += 1

    def delete(self, pos=0) -> bool:
        """删除第pos个元素"""
        if not self.is_pos(pos):
            return False

        d = Node(None, self.head)
        i = 0
        p = d

        while p.next and i != pos:
            p = p.next
            i += 1

        p.next = p.next.next  # 该结点的下一个结点指针指向下下一个结点，即删除下一个结点
        self.head = d.next
        print('delete successfully!')
        return True

    def clear(self) -> bool:
        """清空单链表
        遍历单链表，释放内存"""
        # # 下面的步骤是多余的，即使没有上述步骤，也会有垃圾机制清理掉
        # # 这里只是保留c语言的处理习惯，按照Python的样式重新写了一遍
        # cp = self.head
        # while cp:
        #     np = cp.next
        #     del cp
        #     cp = np
        self.head = None
        print('clear successfully!')
        return True


if __name__ == '__main__':
    link = LinkList()
    data = list(range(3))
    link.init(data)

    print('LinkList\'s length: ', link.length())
    print('original: ', link.traverse())

    for i in range(3, 5):
        link.append(i)
    print('after operate: ', link.traverse())

    link.update(0, 5)
    print('after update(0, 5): ', link.traverse())

    link.delete(0)
    print('after delete(0): ', link.traverse())

    link.insert(0, 7)
    print('after insert(0, 7): ', link.traverse())

    link.sort()
    print('after sort: ', link.traverse())

    link.clear()
    print('after clear: ', link.traverse())

"""
init successfully!
LinkList's length:  3
original:  0 -> 1 -> 2 -> null
after operate:  0 -> 1 -> 2 -> 3 -> 4 -> null
update successfully!
after update(0, 5):  5 -> 1 -> 2 -> 3 -> 4 -> null
delete successfully!
after delete(0):  1 -> 2 -> 3 -> 4 -> null
insert successfully!
after insert(0, 7):  7 -> 1 -> 2 -> 3 -> 4 -> null
sort successfully!
after sort:  1 -> 2 -> 3 -> 4 -> 7 -> null
clear successfully!
after clear:  null
"""
