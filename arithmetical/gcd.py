def euclid(a, b):
    """欧几里得算法，求最大公约数"""
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def extended_euclid(a, b):
    """扩展的欧几里得算法"""
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid(b, a % b)
        d, x, y = d, y, x - a // b * y
        return d, x, y


def stein(a, b):
    """最大公约数"""
    c = 1
    while True:
        if a == 0:
            return b * c
        if b == 0:
            return a * c

        if a % 2 == 0 and b % 2 == 0:
            a >>= 1
            b >>= 1
            c <<= 1
        elif a % 2 == 1 and b % 2 == 1:
            a, b = abs(a - b), min(a, b)
        elif a % 2 == 0:
            a >>= 1
        else:
            b >>= 1


def reduce_fractions(a, b, c):
    """约分带分数，a+b/c -> d/e"""
    g = euclid(c, b)  # 分子分母最大公约数
    # 约分
    c //= g
    b //= g
    b += a * c
    return b, c


def decimal2fractional(x: float) -> (int, int):
    """小数转分数"""
    a, b = str(x).split('.')
    n = len(b)
    if n < 16:  # 非循环小数
        a, b = int(a), int(b)
        c = 10 ** n

        return reduce_fractions(a, b, c)

    else:
        e, f = '', ''  # 非循环体，循环体
        b = b[:-1]  # 最后一位有可能存在精度问题，舍去
        max_n = 0  # 最大循环体长度
        for i in range(n - 1):
            for j in range(i, (n - i) // 2 + 1):
                x, y = b[i: i + j], b[i + j:]
                if x in y:
                    k = y.index(x)
                    e, f = b[:i], b[i:i + j + k]
                    if i + k + 2 * j >= 16:  # 可以确认找到的一定是非循环体和循环体
                        break
            else:
                if not f:  # 循环体还没找到
                    continue

                if max_n < len(f):
                    max_n = len(f)
                    cache_e, cache_f = e, f
                    continue
                else:
                    e, f = cache_e, cache_f
            break

        b = e + f
        a, b = int(a), int(b)
        c = 10 ** len(e) * int('9' * len(f))
        e, f = int(e) if e else 0, int(f) if f else 0
        b -= e

        return reduce_fractions(a, b, c)


def gcd_of_fractions(x: tuple, y: tuple):
    """两个分数的最大公约数"""
    (a, b), (c, d) = x, y
    return reduce_fractions(0, euclid(a, c), b * d // euclid(b, d))


def gcd_multi_int(arr: list):
    """多个数的最大公约数"""
    n = len(arr)
    while True:
        arr = sorted(arr, reverse=True)
        if arr[1] == 0:
            break
        for i in range(n - 1):
            if arr[i + 1] != 0:
                arr[i] = arr[i] % arr[i + 1]

    return arr[0]


if __name__ == '__main__':
    # print(euclid(222, 25653))
    print(extended_euclid(99, 78))
    # print(stein(30, 21))
    # print(gcd_of_fractions((1, 3), (1, 4)))
    # print(gcd_multi_int([4, 8, 12]))
    # for i in range(1, 100):
    #     print(i, decimal2fractional(1 / i), 1 / i)
