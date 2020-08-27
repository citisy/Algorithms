"""字典树，又称单词查找树或键树
它有3个基本性质：
    根节点不包含字符，除根节点外每一个节点都只包含一个字符。
    从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
    每个节点的所有子节点包含的字符都不相同。
字典树是前缀树，可以快速查出单词的公共前缀出现的频率
后缀树是AC自动机
"""


class Node:
    def __init__(self, char, word, children=None, fail=None):
        self.char = char
        self.word = word
        self.children = children or []


class TTree:
    def __init__(self, node=Node):
        self.node = node
        self.mid = self.node(None, 0, '')

    def init(self, arr):
        for a in arr:
            self.insert(a)

    def insert(self, item):
        bn = self.mid
        for j in item:
            # traverse the children, if the item in the children, needn't add the item in the children
            for child in bn.children:
                if j == child.char:
                    break
            else:
                child = self.node(j, '')
                bn.children.append(child)
            bn = child
        bn.word = item

    def find(self, item):
        bn = self.mid
        for j in item:
            for child in bn.children:
                if j == child.char:
                    break
            else:
                return False

            bn = child

        return True if bn.word else False

    def find_all_words(self, bn: Node):
        def recursive(bn):
            if bn:
                if bn.word:  # output the word
                    words.add(bn.word)
            for child in bn.children:
                recursive(child)

        words = set()
        recursive(bn)
        return words

    def find_all_prefix(self, item):
        bn = self.mid
        for j in item:
            for child in bn.children:
                if j == child.char:
                    break
            else:
                return False

            bn = child

        words = set()
        q = [bn]

        while q:
            bn = q.pop()
            for child in bn.children:
                q.append(child)
                if child.word:
                    words.add(child.word)

        return words

    def match(self, item):
        bn = self.mid
        words = []
        for i in item:
            flag = 0
            for child in bn.children:
                if i == child.char:
                    bn = child
                    flag = 1
                    break
            if flag == 0:
                break
            if bn.word:
                words.append(bn.word)
        return words

    def delete(self, item):
        def recursive(bn, i):
            for child in bn.children:
                if item[i] == child.char:
                    break
            else:
                return False

            if i == len(item) - 1:
                child.word = ''
            else:
                return recursive(child, i + 1)

            if not child.children and not child.word:
                bn.children.remove(child)

            return True

        return recursive(self.mid, 0)

    def tree(self, bn: Node):
        """返回二叉树的树形结构"""

        def recursive(bn, dep=0, length=[]):
            if bn:
                stack.append(str(bn.char) + '(%d)' % bool(bn.word))
                if bn.children:
                    child = bn.children[0]
                    if dep >= len(length):
                        length.append(len(str(bn.char)))
                    else:
                        length[dep] = max(length[dep], len(str(bn.char)))
                    dep += 1
                    stack.append('-->')
                    recursive(child, dep, length)
                    for i in range(1, len(bn.children)):
                        child = bn.children[i]
                        s = ''
                        for i in range(dep):
                            s += ' ' * (length[i] + 6)
                        stack.append('\n%s└-->' % s[:-4])
                        recursive(child, dep, length)
            else:
                stack.pop(-1)

        if bn:
            stack = []
            recursive(bn)
            return ''.join(stack)


if __name__ == '__main__':
    a = ['the', 'they', 'them', 'their', 'theirs', 'themselves', 'he', 'hey', 'se', 'self', 'their']
    tt = TTree()
    tt.init(a)
    print('输入序列集合为：')
    print(a)

    print('树形结构为：')
    print(tt.tree(tt.mid))

    print('树中所有以th为前缀的单词：')
    print(tt.find_all_prefix('th'))

    print(tt.find('their'))
    print(tt.find('thea'))

    print(tt.delete('they'))

    print('删除后的树形结构为：')
    print(tt.tree(tt.mid))

    print('删除后树中所有以th为前缀的单词：')
    print(tt.find_all_prefix('th'))

    print(tt.match('themselveself'))

"""
输入序列集合为：
['the', 'they', 'them', 'their', 'theirs', 'themselves', 'he', 'hey', 'se', 'self', 'their']
树形结构为：
None(0)-->t(0)-->h(0)-->e(1)-->y(1)
                           └-->m(1)-->s(0)-->e(0)-->l(0)-->v(0)-->e(0)-->s(1)
                           └-->i(0)-->r(1)-->s(1)
      └-->h(0)-->e(1)-->y(1)
      └-->s(0)-->e(1)-->l(0)-->f(1)
树中所有以th为前缀的单词：
{'them', 'the', 'theirs', 'themselves', 'they', 'their'}
True
False
True
删除后的树形结构为：
None(0)-->t(0)-->h(0)-->e(1)-->m(1)-->s(0)-->e(0)-->l(0)-->v(0)-->e(0)-->s(1)
                           └-->i(0)-->r(1)-->s(1)
      └-->h(0)-->e(1)-->y(1)
      └-->s(0)-->e(1)-->l(0)-->f(1)
删除后树中所有以th为前缀的单词：
{'them', 'the', 'theirs', 'themselves', 'their'}

['the', 'them', 'themselves']
"""
