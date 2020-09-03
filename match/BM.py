def get_bad_character(target):
    """预生成坏字符表"""
    bc = dict()
    for i, char in enumerate(target):
        bc[char] = i + 1  # 记录坏字符最右位置（不包括模式串最右侧字符）
    return bc


def get_good_suffix(target):
    """预生成好后缀表"""
    gs = dict()
    gs[''] = 0  # 无后缀仅根据坏字移位符规则
    m = len(target)
    for i in range(m):
        suffix = target[m - i - 1:]  # 好后缀

        for j in range(m - i - 1):
            non_suffix = target[j:j + i + 1]  # 匹配部分

            if suffix == non_suffix:  # 记录模式串中好后缀最靠右位置（除结尾处）
                gs[suffix] = m - j - i - 1
    return gs


def match(source, target):
    if not source or not target:
        return -1

    n, m = len(source), len(target)
    if n < m:
        return -1

    i, j = 0, m
    bc = get_bad_character(target)  # 坏字符表
    gs = get_good_suffix(target)  # 好后缀表

    while i < n and j > 0:
        a, b = source[i + j - 1], target[j - 1]

        if a == b:  # 当前位匹配成功则继续匹配
            j = j - 1

        else:  # 当前位匹配失败根据规则移位

            # 这里，坏字符有可能出现负移动的情况，这是因为程序偷懒，没有判断最右位置的坏字符可能会出现当前位置的右侧的情况
            # 但由于还有好后缀的制衡，最终答案还是正确，反而代码变得更加优雅
            i += max(j - bc.setdefault(a, 0), gs.setdefault(target[j:], m))
            j = m

    if j == 0:
        return i
    else:
        return -1


if __name__ == '__main__':
    s = 'BBC ABEDA ABCDABCDABDE'
    p = 'ABCDABD'
    pos = match(s, p)
    print(pos)
    print(s[pos: pos + len(p)])
