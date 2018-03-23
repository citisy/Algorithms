# -*- coding: utf-8 -*-

# 创建一个保存data和head的对象，模拟单链表


class Node():
    def __init__(self, data, next=None):
        '''
        data: 数据域
        next: 结点指针
        '''
        self.data = data
        self.next = next

    def __repr__(self):
        '''
        print(Node)=>data
        '''
        return str(self.data)

class LinkList():
    '''
    functions：
        is_empty(): 判断是否为空
        init(data): 初始化单链表
        lenth(): 返回单链表长度
        get(pos): 取第pos个元素
        traverse(): 遍历单链表并打印
        find(item): 查找单链表某值的位置
        update(pos, item): 更新第pos个结点
        insert(pos, item): 在pos位置后插入元素
        append(item): 单链表结尾添加一个元素
        delete(pos): 删除第pos个元素
        clear(): 清空单链表
    '''
    def __init__(self):
        self.head = None  # 头结点

    # 判断是否为空
    def is_empty(self):
        return self.head == None

    # 初始化单链表
    def init(self, data):
        if self.is_empty():
            self.head = Node(data[0])  # 初始化头结点
            p = self.head
            for i in data[1:]:
                p.next = Node(i)
                p = p.next  # 结点指针指向下一结点

    # 返回单链表长度
    def lenth(self):
        if self.is_empty():
            print('linklist is empty')
            return None
        i = 1
        p = self.head
        while p.next:
            i += 1
            p = p.next
        return i

    # 取第pos个元素
    def get(self, pos):
        # 判断pos是否符合要求
        if pos < 1:
            print('error: pos<1')
            exit(1)
        elif pos > self.lenth():
            print('error: pos out of range')
            exit(1)
        i = 1
        p = self.head
        while p:
            if i == pos:
                return p.data
            p = p.next
            i += 1

    # 遍历单链表并打印
    def traverse(self):
        p = self.head
        while p:
            print(p, end=' ')
            p = p.next
        print()

    # 查找单链表某值的位置
    def find(self, item):
        p = self.head
        pos = 1
        while p:
            if item == p.data:
                return pos
            pos += 1
        print('not found!')
        return None

    # 更新第pos个结点
    def update(self, pos, item):
        # 判断pos是否符合要求
        if pos < 1:
            print('error: pos<1')
            exit(1)
        elif pos > self.lenth():
            print('error: pos out of range')
            exit(1)
        i = 1
        p = self.head
        while p:
            if i == pos:
                p.data = item
                return print('update successfully!')
            i += 1
            p = p.next

    # 在pos位置后插入元素
    def insert(self, pos, item):
        # 判断pos是否符合要求
        if pos < 0:
            print('error: pos<0')
            exit(1)
        elif pos > self.lenth():
            print('error: pos out of range')
            exit(1)
        # 插入元素创建新结点
        newp = Node(item)
        # 插入到表头
        if pos == 0:
            newp.next = self.head.next
            self.head.next = newp
            return print('insert successfully!')
        i = 1
        p = self.head
        while p:
            if i == pos:
                newp.next = p.next
                p.next = newp
                return print('insert successfully!')
            p = p.next
            i += 1

    # 单链表结尾添加一个元素
    def append(self, item):
        # 链表为空
        if self.is_empty():
            self.head = Node(item)
        else:
            newp = Node(item)
            p = self.head
            while p.next:
                p = p.next
            p.next = newp

    # 删除第pos个元素
    def delete(self, pos):
        # 判断pos是否符合要求
        if pos < 0:
            print('error: pos<0')
            exit(1)
        elif pos > self.lenth():
            print('error: pos out of range')
            exit(1)
        # 删除表头结点
        elif pos == 0:
            q = self.head.next
            self.head = q
            return print('delete successfully!')
        i = 1
        p = self.head
        q = p  # 保存p的指针
        while p:
            if i == pos:
                # 该结点的上一个结点指针指向下一个结点，即删除该结点
                q.next = p.next
                return print('delete successfully!')
            q = p
            p = p.next
            i += 1

    # 清空单链表
    # 遍历单链表，释放内存
    def clear(self):
        cp = self.head
        while cp:
            np = cp.next
            del cp
            cp = np
        self.head = None
        return print('clear successfully!')


if __name__ == '__main__':
    link = LinkList()
    data = range(3)
    link.init(data)
    for i in range(3, 5):
        link.append(i)
    link.traverse()
    print('linklist\'s length: ', str(link.lenth()))
    link.update(3, 5)
    link.delete(4)
    link.insert(3, 7)
    link.traverse()
    link.clear()
    print(link.is_empty())
