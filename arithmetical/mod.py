from gcd import extended_euclid


def modular_exponentiation(a, b, n):
    """幂数模，a ^ b % n """
    d = 1
    b = bin(b)[2:]
    k = len(b)
    for i in range(k):
        d = (d ** 2) % n
        if b[i] == '1':
            d = (d * a) % n
    return d


def Chinese_remainder_theorem(m: list, a: list):
    """中国余数定理"""
    s = 1
    for mm in m:
        s *= mm

    r = 0
    for i, mm in enumerate(m):
        mi = s // mm

        d, x, y = extended_euclid(mi, mm)

        if d != 1:  # 说明不互质，程序无结果
            return -1

        ti = x
        r += a[i] * ti * mi

    return r % s


if __name__ == '__main__':
    print(Chinese_remainder_theorem([9, 8, 7], [1, 2, 3]))
