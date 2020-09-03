def match(source, target):
    if not source or not target:
        return -1

    n, m = len(source), len(target)
    if n < m:
        return -1

    i, j = 0, 0
    while i < n and j < m:
        if source[i] == target[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

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