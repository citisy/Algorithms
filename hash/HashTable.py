import numpy as np


class HashTable:
    def __init__(self, m=None):
        self.m = m

    def init(self, arr, hash_func=None, hash_args=(), collision=False, coll_func=None, coll_args=()):
        """仅支持单个英文字符或数字"""
        self.hash_func = hash_func or self.hash_func_mod_remain
        self.hash_args = hash_args or (arr, None, None)
        self.coll_func = coll_func or self.coll_func_linear_detect
        self.collision = collision
        self.coll_args = coll_args

        arr = [a if isinstance(a, int) else ord(a) for a in arr]
        n = len(arr)

        if not self.m:
            if self.hash_func == self.hash_func_straight_search:
                self.m = 2 * len(arr)

            elif self.hash_func == self.hash_func_number_analysis:
                self.m = 2 ** int(np.ceil(np.log2(n / 0.75)))

            elif self.hash_func == self.hash_func_square_middle:
                self.m = 10 ** int(np.ceil(np.log10(n / 0.75)))

            elif self.hash_func == self.hash_func_fold_sum:
                self.m = 10 ** int(np.ceil(np.log10(n / 0.75)))

            elif self.hash_func == self.hash_func_mod_remain:
                self.m = 2 ** int(np.ceil(np.log2(n / 0.75)))
                self.m = self.find_prime_number(self.m)

            elif self.hash_func == self.hash_func_decimal_remain:
                self.m = 2 ** int(np.ceil(np.log2(n / 0.75)))

            elif self.hash_func == self.hash_func_universal:
                self.m = int(n / 0.75)

        self.table = [None for _ in range(self.m)] if collision else [[] for _ in range(self.m)]

        for a in arr:
            self.add(a)

    def add(self, k):
        idx, self.hash_args = self.hash_func(k, *self.hash_args)
        if self.collision:
            idx = self.coll_func(idx, True, None, *self.coll_args)
            self.table[idx] = k
        else:
            self.table[idx].append(k)

    def search(self, k):
        idx, _ = self.hash_func(k, *self.hash_args)

        if not self.table[idx]:
            return -1

        if self.collision:
            idx = self.coll_func(idx, False, k, *self.coll_args)
            return idx
        else:
            for i, kk in enumerate(self.table[idx]):
                if kk == k:
                    return idx, i

    def delete(self, k):
        idx = self.search(k)

        if self.collision:
            self.table[idx] = None
        else:
            self.table[idx[0]].pop(idx[1])

        return idx

    def hash_func_straight_search(self, k, arr=None, a=None, b=None, *args):
        """直接寻址法
        a: 斜率
        b: 截距"""
        if a is None:
            m = self.m - 1
            max_a = max(arr)
            min_a = min(arr)
            a = m / (max_a - min_a)
            b = -m * min_a / (max_a - min_a)

        return int(k * a + b), (arr, a, b)

    def hash_func_number_analysis(self, k, arr=None, bit_map=None, max_b=None, *args):
        """数字分析法
        bit_map: 取哪几位二进制
        max_b: 最大值的位数"""
        if bit_map is None:
            max_b = max_b or 0
            bit = int(np.ceil(np.log2(self.m)))  # 取多少位
            bin_arr = []
            for a in arr:
                x = [int(i) for i in bin(a)[2:]]
                max_b = max(len(x), max_b)
                bin_arr.append(x)

            for i, a in enumerate(bin_arr):
                bin_arr[i] = [0] * (max_b - len(a)) + a

            bin_arr = np.array(bin_arr, dtype=int)
            bit_map = np.argsort(np.abs(np.sum(bin_arr, axis=0) - len(arr) / 2))[:bit]

        bin_k = [int(i) for i in bin(k)[2:]]
        max_b = max(len(bin_k), max_b)
        bin_k = [0] * (max_b - len(bin_k)) + bin_k
        bin_k = np.array(bin_k, dtype=int)
        idx = ''
        for _ in bin_k[bit_map]:
            idx += str(_)
        idx = int(idx, 2)

        return idx, (arr, bit_map, max_b)

    def hash_func_square_middle(self, k, arr=None, a=None, b=None, *args):
        """平方取中法
        a: 最低位
        b: 取多少位"""
        if a is None:
            min_a = min(arr)
            bit = int(np.ceil(np.log10(self.m)))
            n = len(str(min_a))
            a = 10 ** ((n - bit) // 2)
            b = 10 ** bit

        idx = k // a % b
        return idx, (arr, a, b)

    def hash_func_fold_sum(self, k, arr=None, b=None, *args):
        """折叠求和法
        b: 每b位切成一部分"""
        if b is None:
            bit = int(np.ceil(np.log10(self.m)))
            b = 10 ** bit

        idx = 0
        while k:
            idx = (idx + k % b) % b
            k //= b

        return idx, (arr, b)

    def hash_func_mod_remain(self, k, arr=None, q=None, *args):
        """除留余数法
        q: 除数"""
        if q is None:
            q = self.find_prime_number(self.m)

        return k % q, (arr, q)

    def hash_func_decimal_remain(self, k, arr=None, s=None, w=None, *args):
        """乘留小数法
        s: 未知参数
        w: 最大关键字的位数"""
        if s is None:
            max_a = max(arr)
            w = int(np.ceil(np.log2(max_a)))
            s = int(2 ** w * (5 ** 0.5 - 1) / 2)
            w = 2 ** w

        idx = int(k * s % w / w * self.m)

        return idx, (arr, s, w)

    def hash_func_universal(self, k, arr=None, p=None, a=None, b=None, *args):
        """全域散列法"""
        if p is None:
            max_a = max(arr)
            p = max_a + 1
            a, b = np.random.randint(max_a, size=2)

        idx = (a * k + b) % p % self.m

        return idx, (arr, p, a, b)

    def coll_func_linear_detect(self, idx, add=True, k=None, *args):
        """线性探测法"""
        for i in range(idx, self.m):
            if (self.table[i] is None and add) or (self.table[i] == k and not add):
                return i
        for i in range(idx):
            if (self.table[i] is None and add) or (self.table[i] == idx and not add):
                return i

        raise MemoryError('Hash table is full!')

    def coll_func_square_detect(self, idx, add=True, k=None, *args):
        """二次探测法"""
        for i in range(int(np.ceil(np.sqrt(self.m)))):
            ii = i ** 2 + idx
            if ii < self.m:
                if (self.table[ii] is None and add) or (self.table[ii] == k and not add):
                    return ii
            ii = -(i ** 2) + idx
            if ii < self.m:
                if (self.table[ii] is None and add) or (self.table[ii] == k and not add):
                    return ii

        raise MemoryError('Hash table is full!')

    def coll_func_random_detect(self, idx, add=True, k=None, *args):
        """伪随机探测法"""
        cache = [idx]
        while True:
            if (self.table[idx] is None and add) or (self.table[idx] == k and not add):
                return idx
            idx = np.random.randint(self.m)
            if idx in cache and len(cache) == self.m:
                raise MemoryError('Hash table is full!')

            cache.append(idx)

    def find_prime_number(self, k):
        """寻找不大于k的素数"""
        for i in range(k, 0, -1):
            for j in range(2, int(np.sqrt(k)) + 1):
                if i % j == 0:
                    break
            else:
                return i


if __name__ == '__main__':
    np.random.seed(0)

    ht = HashTable()
    arr = np.random.randint(11000, 12000, 10)
    arr = [int(a) for a in arr]
    print(arr)

    ht.init(arr,
            hash_func=ht.hash_func_universal,
            collision=False,
            coll_func=ht.coll_func_linear_detect)

    print(ht.table)
    for a in arr:
        print(ht.search(a))

    for a in arr:
        ht.delete(a)
        print(ht.table)
