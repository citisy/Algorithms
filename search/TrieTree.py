"""字典树，又称单词查找树或键树
它有3个基本性质：
    根节点不包含字符，除根节点外每一个节点都只包含一个字符。
    从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
    每个节点的所有子节点包含的字符都不相同。
字典树是前缀树，可以快速查出单词的公共前缀出现的频率
后缀树是AC自动机
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.fail = None    # Aho-Corasick algorithms will use this param


class TTree:
    def __init__(self):
        self.mid = Node([None, 0, ''])
        self.dic = {}  # {word: count}
        self.cache = ['' for _ in range(20)]

    def init(self, arr):
        for i, a in enumerate(arr):
            bn = self.mid
            for j in a:
                flag = 0
                # traverse the children, if the item in the children, needn't add the item in the children
                for child in bn.children:
                    if j == child.data[0]:
                        flag = 1
                        break
                if flag == 0:
                    child = Node([j, 0, ''])
                    bn.children.append(child)
                bn = child
            bn.data[1] += 1  # when the word is end, the count++
            bn.data[2] = a

    def traverse(self, bn):
        if bn:
            if bn.data[1] != 0:  # output the word
                self.dic[bn.data[2]] = bn.data[1]
        for child in bn.children:
            self.traverse(child)

    def search(self, item):
        bn = self.mid
        words = []
        for i in item:
            flag = 0
            for child in bn.children:
                if i == child.data[0]:
                    bn = child
                    flag = 1
                    break
            if flag == 0:
                break
            if bn.data[1] != 0:
                words.append(bn.data[2])
        return words


if __name__ == '__main__':
    a = ['the', 'they', 'them', 'their', 'theirs', 'themselves', 'he', 'hey', 'se', 'self', 'their']
    tt = TTree()
    tt.init(a)
    tt.traverse(tt.mid)
    print(tt.dic)

    words = tt.search('themselveself')
    print(words)

"""
{'the': 1, 'hey': 1, 'their': 1, 'self': 1, 'them': 1, 'they': 1, 'se': 1, 'he': 1, 'themselves': 1, 'theirs': 1}
['the', 'them', 'themselves']
"""
