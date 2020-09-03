def match(source, target):
    if not source or not target:
        return -1

    n, m = len(source), len(target)
    if n < m:
        return -1

    bc = {}     # 坏字符表

    for i, char in enumerate(target):
        bc[char] = m - i

    i, j = 0, 0

    while i <= n - m and j < m:
        if source[i + j] == target[j]:
            j += 1
        else:
            i += bc.setdefault(source[i + m], m + 1)
            j = 0

    if j == m:
        return i
    else:
        return -1


if __name__ == '__main__':
    s = 'BBC ABEDA ABCDABCDABDE'
    p = 'ABCDABD'
    pos = match(s, p)
    print(pos)
    print(s[pos: pos + len(p)])
