"""二分查找。输入数据必须是顺序表，默认从小到大排序。"""


def binsch(arr, l, h, k):
    """在arr[l]-arr[h]中寻找k"""
    if l <= h:
        # 寻找中点坐标
        mid = (l + h) // 2

        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            return binsch(arr, l, mid - 1, k)
        else:
            return binsch(arr, mid + 1, h, k)
    else:
        return -1


if __name__ == '__main__':
    a = range(10)
    i = binsch(a, 0, 9, 7)
    print('元素为 7 的下标：', i)
    print('下标是 %d 的元素: %d' % (i, a[i]))

"""
元素为7的下标： 7
下标是 7 的元素: 7
"""
