import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        res = [1] * n
        res[0] = 0
        res[1] = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if res[i] == 1:
                for j in range(i + i, n, i):
                    res[j] = 0
        return sum(res)