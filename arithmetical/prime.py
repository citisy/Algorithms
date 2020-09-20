import random
from gcd import euclid
from mod import modular_exponentiation


def pseudo_prime(n, a=2):
    """伪素数测试"""
    if modular_exponentiation(a, n - 1, n) % n != 1:
        return False
    else:
        return True


def miller_rabin(n, s=10):
    """素数测试"""

    def witness(a):
        #  n-1 的二进制表示是奇数 u 的二进制表示后面跟上 t 个零。
        b = bin(n - 1)[2:]
        t = 0
        for i in range(len(b) - 1, -1, -1):
            if b[i] == '1':
                break
            t += 1

        u = int(b[:len(b) - t], 2)

        x = modular_exponentiation(a, u, n)
        y = x
        for i in range(t):
            x = (y ** 2) % n
            if x == 1 and y != 1 and y != n - 1:
                return False
            y = x

        if x != 1:
            return False

        return True

    if n == 2 or n == 3:  # 特判
        return True
    if n % 2 == 0 or n == 1:
        return False

    for j in range(s):
        a = random.randint(1, n - 1)
        if not witness(a):
            return False
    return True


def pollard_rho(a):
    """质因数分解"""

    def recursive(n):
        x = random.randint(0, n - 1)
        y = x
        i, k = 1, 2
        while True:
            i += 1
            x = (x ** 2) % n + i

            d = euclid(y - x, n)
            if d != 1 and d != n:
                return d
            if y == x:
                return n
            if i == k:
                y = x
                k <<= 1

    r = []
    q = [a]
    while q:
        a = q.pop()
        if a == 1:
            continue
        if miller_rabin(a):
            r.append(a)
        else:
            b = recursive(a)
            a //= b
            q.append(a)
            q.append(b)

    return r


def find_prime(max_n):
    """寻找 [2,max_n] 区间内的质数"""

    r = list(range(2, max_n + 1))
    i = 0
    while i < len(r):
        r = r[:i] + list(filter(lambda x: x == r[i] or x % r[i], r[i:]))
        i += 1

    return r


if __name__ == '__main__':
    # print(modular_exponentiation(7, 560, 561))
    # print(pseudo_prime(2, 27))
    # print(miller_rabin(5))
    # print(pollard_rho(5))
    # for i in range(2, 100):
    #     # print(i, miller_rabin(i))
    #     print(i, pollard_rho(i))
    print(find_prime(10000))
