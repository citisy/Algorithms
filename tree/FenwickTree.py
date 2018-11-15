class FTree:
    def __init__(self, size):
        """
        Fenwick tree，also named binary indexed tree
        use array to save the tree
        there is a Fenwick tree, remember, the tree start with the index of 1:

        1   2   3   4   5   6   7   8
        x       x       x       x
        ----x           ----x
        ------------x
        ----------------------------x

        1 is 2's children, 1 & 3 is 4's children, 4, 6 & 7 is 8's children ,and so on
        we 'pull' the tree to left, so that,
        when update x(i) to 1, query(j), j>=i would add 1, too
        eg:
            update(i)=1 -> x(i)=1, i=2 -> query(j)=1, j>=i,
            update(i+2)=2 -> x(i+2)=2, i=2 -> query(j)=1, i<=j<i+2, query(j)=3, j>=i+2,
            and so on
        """
        self.size = size + 1
        self.ft = [0 for _ in range(self.size)]

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

    def update(self, i, value):
        if i >= self.size:
            return None
        while i < self.size:
            self.ft[i] += value
            i += self.lowbit(i)

    def query(self, i):
        if i >= self.size:
            return None
        ret = 0
        while i > 0:
            ret += self.ft[i]
            i -= self.lowbit(i)
        return ret


if __name__ == '__main__':
    f = FTree(8)
    print('before update: ', end=' ')
    for i in range(1, 9):
        print(f.query(i), end=' ')
    print()

    f.update(2, 1)
    f.update(4, 2)
    print('after update: ', end=' ')
    for i in range(1, 9):
        print(f.query(i), end=' ')

"""
before update:  0 0 0 0 0 0 0 0 
after update:  0 1 1 3 3 3 3 3 
"""