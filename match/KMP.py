"""http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html"""


def get_next(target):
    m = [0 for _ in range(len(target))]
    m[0] = -1
    k, j = -1, 0
    while j < len(target) - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            if p[j] != p[k]:
                m[j] = k
            else:
                m[j] = m[k]
        else:
            k = m[k]

    return m


def search(source, target):
    if not target:
        return 0

    nextj = get_next(target)
    print(nextj)
    i, j = 0, 0
    while i < len(source) and j < len(target):
        if j == -1 or source[i] == target[j]:
            i += 1
            j += 1
        else:
            j = nextj[j]
    if j == len(target):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    s = 'BBC ABCDA ABCDABCDABDE'
    p = 'ABCDABD'
    pos = search(s, p)
    print(pos)
    print(s[pos: pos + len(p)])
