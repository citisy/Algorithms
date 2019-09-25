"""AC自动机
算法总体流程：
    1.建立模式的Trie
    2.给Trie添加失败路径
    3.根据AC自动机，搜索待处理的文本
添加失败路径步骤：
    1.沿着某一节点C的父亲的失败指针走，直到走到一个节点，他的儿子中也有字母为C的节点。
    2.把当前节点的失败指针指向那个字母也为C的儿子。
    3.如果一直走到了root都没找到，那就把失败指针指向root。
搜索步骤：
    1.从root节点开始，每次根据读入的字符沿着自动机向下移动。
    2.当读入的字符，在分支中不存在时，递归走失败路径。
    3.如果走失败路径走到了root节点，则跳过该字符，处理下一个字符。
参考博客：
    http://www.hankcs.com/program/algorithm/implementation-and-analysis-of-aho-corasick-algorithm-in-java.html
    https://www.cnblogs.com/xudong-bupt/p/3433506.html
"""

from TrieTree import TTree


class ACT:
    def __init__(self):
        self.tree = TTree()
        self.char = []
        self.word = []
        self.children = []
        self.fail = []
        self.output = []

    def init(self, arr):
        self.tree.init(arr)
        self.mid = self.tree.mid
        self.mid.fail = self.mid
        q = []
        for child in self.mid.children:  # in particular, the second floor's fail point to the mid node
            child.fail = self.mid
            q.append([child, self.mid])  # [child, parent]
        while len(q) != 0:
            bn, parent = q.pop(0)
            for child in bn.children:
                q.append([child, bn])
            self.add_fail(bn, parent)
        self.tree2list()

    def add_fail(self, bn, parent):
        """levelorder traverse the tree, add the fail point"""
        while parent.fail is not parent:  # only root's fail point to his own
            for child in parent.fail.children:
                if bn.data[0] == child.data[0]:  # bn's data -> [char, count, word]
                    bn.fail = child
                    return
            parent = parent.fail  # can't find item in bn's fail's children, point to fail's fail
        if bn.fail is None:  # can't find item until the root, point to the root
            bn.fail = self.mid

    def get_bn(self, data, bn):
        """
        :return:
            data can find in bn's children -> bn which data equaled to data
            data can't find and bn is root -> root
            data can't find and bn is not root -> None
        """
        for child in bn.children:
            if data == child.data[0]:
                bn = child
                return bn
        if bn is self.mid:
            return bn
        else:
            return None

    def tree2list(self):
        i = 1
        p = [(self.mid, i)]
        i += len(self.mid.children)
        pp = []
        while len(p) > 0:
            pn, index = p.pop(0)
            for child in pn.children:
                p.append((child, i))
                i += len(child.children)
            pp.append(pn)
            self.char.append(pn.data[0])
            self.word.append(pn.data[2])
            self.output.append(pn.data[1])
            self.fail.append(pp.index(pn.fail))
            self.children.append((index, index + len(pn.children)))

    def search(self, item, index=False):
        bn = self.mid
        words = []
        for i, data in enumerate(item):
            while 1:
                n = self.get_bn(data, bn)
                if n is self.mid:
                    break
                if n is not None:
                    bn = n
                    break
                bn = bn.fail  # run it means find not success, turn to bn's fail
            if bn.data[1]:
                if index:
                    words.append([bn.data[2], i + 1 - len(bn.data[2])])   # [word, start_index]
                else:
                    words.append(bn.data[2])
            if bn.fail.data[1]:
                if index:
                    words.append([bn.fail.data[2], i + 1 - len(bn.fail.data[2])])   # [word, start_index]
                else:
                    words.append(bn.fail.data[2])
        return words

    def fast_search(self, item):
        bn = 0
        words = []
        for char in item:
            while 1:
                st, et = self.children[bn]
                for n, c in enumerate(self.char[st: et]):
                    if char == c:
                        break
                else:
                    n = -1
                if n != -1:
                    bn = st + n
                    break
                else:
                    if bn == 0:
                        break
                    bn = self.fail[bn]
            if self.output[bn]:
                words.append(self.word[bn])
            if self.output[self.fail[bn]]:
                words.append(self.word[self.fail[bn]])
        return words


if __name__ == '__main__':
    a = ['the', 'they', 'them', 'their', 'theirs', 'themselves', 'he', 'hey', 'se', 'self']
    s = 'thuthemselveselftheirthey'
    ac = ACT()
    ac.init(a)

    words = ac.fast_search(s)
    print(words)

"""
result:
[['the', 3], ['them', 3], ['themselves', 3], ['se', 12], ['self', 12], ['the', 16], ['their', 16]]
"""
