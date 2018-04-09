# -*- coding: utf-8 -*-

# 索引查找。
# 索引表中每个索引项有三个域：索引值域(index)、开始位置域(start)、子表长度域(length)
# 主表和索引表需要自己编写


class IndexItem():
    def __init__(self, index, start, length):
        self.index = index
        self.start = start
        self.length = length


def indsch(ml, il, k1, k2):
    '''
    :param ml: 主表
    :param il: 索引表
    :param k1: 索引值
    :param k2: 查找值
    :return: 查找成功返回元素的下标，否则返回-1
    '''
    n = len(il.index)
    # i => 查找k1在索引表的下标
    for i in range(n):
        if k1 == il.index[i]:
            break
    # j => 查找k2在主表的下标
    j = il.start[i]
    while j < il.start[i] + il.length[i]:
        if k2 == ml[j]:
            break
        else:
            j += 1
    # 查找成功返回下标，否则返回-1
    if j < il.start[i] + il.length[i]:
        return j
    else:
        return -1


if __name__ == '__main__':
    mainlist = ['js001', 'js002', 'js003', 'js004',
                'dz001', 'dz002', 'dz003',
                'jj001', 'jj002',
                'hg001', 'hg002', 'hg003']
    index = ['js', 'dz', 'jj', 'hg']
    start = [0, 4, 7, 9]
    length = [4, 3, 2, 3]
    indexlist = IndexItem(index, start, length)
    i = indsch(mainlist, indexlist, 'dz', 'dz002')
    print('dz002的下标：', i)
    print('主表下标为 %d 的元素： %s' % (i, mainlist[i]))
