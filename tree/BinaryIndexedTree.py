import math


class FTree:
    """
    Binary indexed tree, also named Fenwick tree
    use array to save the tree
    there is a Fenwick tree, remember, the tree start with the index of 1:

                ----------------------------36
                ------------10
                ----3           ----11
    tree        1       3       5       7
                -----------------------------
    array_index 1   2   3   4   5   6   7   8

    1 is 2's children, 1 & 3 is 4's children, 4, 6 & 7 is 8's children ,and so on
    we 'pull' the tree to the left, so that,
    when update x(i) to 1, query(j), j>=i would add 1, too
    eg:
        update(i)=1 -> x(i)=1, i=2 -> query(j)=1, j>=i,
        update(i+2)=2 -> x(i+2)=2, i=2 -> query(j)=1, i<=j<i+2, query(j)=3, j>=i+2,
        and so on
    """
    def init(self, arr: list):
        self.size = 2 ** math.ceil(math.log2(len(arr))) + 1
        self.ft = [0] * self.size
        for i, a in enumerate(arr):
            self.update(a, i + 1)

    def lowbit(self, i):
        """
        change the number to binary, and then remove the '1' , the firstly appear on the right, whose left area.
        i + lowbit(i) = 2 ^ (int(sqrt(i)) + 1)
        eg:
            14 -> 1110
            the 3-bit '1' is the firstly appear on the right, remove '11', and left '10'
            so, lowbit(14) = 2
        """
        return i & (-i)

    def update(self, value, i):
        if i >= self.size:
            return None
        while i < self.size:
            self.ft[i] += value
            i += self.lowbit(i)

    def query(self, l, r=None):
        def func(i):
            if i >= self.size:
                return None
            ret = 0
            while i > 0:
                ret += self.ft[i]
                i -= self.lowbit(i)
            return ret

        if r:
            return func(r + 1) - func(l)
        else:
            return func(l + 1)


if __name__ == '__main__':
    a = list(range(10))
    print("输入序列:", a)
    st = FTree()
    st.init(a)
    print('构建的线索树:')
    print(st.ft)
    print('query area [2, 5] is %d' % st.query(2, 5))
    st.update(0, 10)
    print('after update:')
    print(st.ft)

"""
输入序列: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
构建的线索树:
[0, 0, 1, 2, 6, 4, 9, 6, 28, 8, 17, 0, 17, 0, 0, 0, 45]
query area [2, 5] is 14
after update:
[0, 0, 1, 2, 6, 4, 9, 6, 28, 8, 17, 0, 17, 0, 0, 0, 45]
"""