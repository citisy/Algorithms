def get_next(target):
    m = [0 for _ in range(len(target))]
    for i in range(len(target)):
        _ = target[:i]
        for j in range(i):
            if _[:j] == _[-j:]:
                m[i] = j
    m[0] = -1
    return m


def search(source, target):
    if not target:
        return 0

    nextj = get_next(target)
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
    s = 'source'
    p = 'target'
    pos = search(s, p)
    print(pos)
    print(s[pos: pos + len(p)])
