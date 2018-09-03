"""散列查找、哈希查找
对于关键字k，以函数h（k）计算其函数值，并保存在连续存储空间。
如果待插入元素的位置已经被占用，则会发生冲突。
如每个存储空间为1时，当h（k）=k%5，则1和6的都要存储在位置为1的空间下，就会发生冲突。

构造哈希函数的方法：直接定址法
除留余数法
数字分析法
平方取中法
折叠法

处理冲突的方法：
开发定址法
链接法
"""



class Node(object):
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


class LinkHashList(object):
    def __init__(self):
        pass

    def init(self):
        pass

    def clear(self):
        pass

    def insert(self):
        pass

    def search(self):
        pass

    def delete(self):
        pass


class ArrayHashList(object):
    def __init__(self):
        pass

    def init(self):
        pass

    def clear(self):
        pass

    def insert(self):
        pass

    def search(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    pass