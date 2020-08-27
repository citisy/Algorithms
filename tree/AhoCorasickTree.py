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


class Node:
    def __init__(self, char, word, children=None, fail=None):
        self.char = char
        self.word = word
        self.children = children or []
        self.fail = fail


class ACT(TTree):
    def __init__(self, node=Node):
        super(ACT, self).__init__(node)
        self.char = []
        self.word = []
        self.children = []
        self.fail = []
        self.mid.fail = self.mid

    def init(self, arr):
        super(ACT, self).init(arr)

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
                if bn.char == child.char:  # bn's data -> [char, count, word]
                    bn.fail = child
                    return
            parent = parent.fail  # can't find item in bn's fail's children, point to fail's fail

        else:  # can't find item until the root, point to the root
            bn.fail = self.mid

        return bn

    def get_bn(self, data, bn):
        """
        :return:
            data can find in bn's children -> bn which data equaled to data
            data can't find and bn is root -> root
            data can't find and bn is not root -> None
        """
        for child in bn.children:
            if data == child.char:
                bn = child
                return bn
        if bn is self.mid:
            return bn

    def match(self, item, index=False):
        bn = self.mid
        words = []
        success = 0
        for i, data in enumerate(item):
            while 1:
                for child in bn.children:
                    if data == child.char:
                        bn = child
                        success = 1
                        break

                if bn is self.mid:
                    break
                elif success:
                    success = 0
                    break
                else:
                    bn = bn.fail

            if bn.word:
                if index:
                    words.append((bn.word, i + 1 - len(bn.word)))  # [word, start_index]
                else:
                    words.append(bn.word)

            if bn.fail.word:
                if index:
                    words.append((bn.fail.word, i + 1 - len(bn.fail.word)))  # [word, start_index]
                else:
                    words.append(bn.fail.word)
        return words

    def tree2list(self):
        i = 1
        p = [(self.mid, i)]
        i += len(self.mid.children)
        pp = []
        while p:
            pn, index = p.pop(0)
            for child in pn.children:
                p.append((child, i))
                i += len(child.children)
            pp.append(pn)
            self.char.append(pn.char)
            self.word.append(pn.word)
            self.fail.append(pp.index(pn.fail))
            self.children.append((index, index + len(pn.children)))

    def fast_match(self, item, index=False):
        idx = 0
        words = []
        for i, data in enumerate(item):
            while 1:
                st, et = self.children[idx]
                for n, c in enumerate(self.char[st: et]):
                    if data == c:
                        break
                else:
                    n = -1

                if n != -1:
                    idx = st + n
                    break
                elif idx == 0:
                    break
                else:
                    idx = self.fail[idx]

            if self.word[idx]:
                if index:
                    words.append((self.word[idx], i + 1 - len(self.word[idx])))  # [word, start_index]
                else:
                    words.append(self.word[idx])

            if self.word[self.fail[idx]]:
                if index:
                    words.append((self.word[self.fail[idx]], i + 1 - len(self.word[self.fail[idx]])))
                else:
                    words.append(self.word[self.fail[idx]])

        return words


if __name__ == '__main__':
    a = ['the', 'they', 'them', 'their', 'theirs', 'themselves', 'he', 'hey', 'se', 'self']
    s = 'thuthemselveselftheirthey'
    ac = ACT()
    ac.init(a)
    print(ac.tree(ac.mid))
    print(ac.match(s, True))
    print(ac.fast_match(s, True))

"""
None(0)-->t(0)-->h(0)-->e(1)-->y(1)
                           └-->m(1)-->s(0)-->e(0)-->l(0)-->v(0)-->e(0)-->s(1)
                           └-->i(0)-->r(1)-->s(1)
      └-->h(0)-->e(1)-->y(1)
      └-->s(0)-->e(1)-->l(0)-->f(1)
[('the', 3), ('he', 4), ('them', 3), ('se', 7), ('themselves', 3), ('se', 12), ('self', 12), ('the', 16), ('he', 17), ('their', 16), ('the', 21), ('he', 22), ('they', 21), ('hey', 22)]
[('the', 3), ('he', 4), ('them', 3), ('se', 7), ('themselves', 3), ('se', 12), ('self', 12), ('the', 16), ('he', 17), ('their', 16), ('the', 21), ('he', 22), ('they', 21), ('hey', 22)]
"""
