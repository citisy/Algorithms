"""http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html"""


def get_next(target):
    next_ = [0 for _ in range(len(target))]
    next_[0] = -1
    k, j = -1, 0
    while j < len(target) - 1:
        if k == -1 or target[j] == target[k]:
            j += 1
            k += 1
            if target[j] != target[k]:
                next_[j] = k
            else:
                next_[j] = next_[k]
        else:
            k = next_[k]

    return next_


def match(source, target):
    if not source or not target:
        return -1

    n, m = len(source), len(target)
    if n < m:
        return -1

    next_ = get_next(target)
    i, j = 0, 0
    while i < n and j < m:
        if j == -1 or source[i] == target[j]:
            i += 1
            j += 1
        else:
            j = next_[j]
    if j == len(target):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    s = 'BBC ABCDA ABCDABCDABDE'
    p = 'ABCDABD'
    pos = match(s, p)
    print(pos)
    print(s[pos: pos + len(p)])
