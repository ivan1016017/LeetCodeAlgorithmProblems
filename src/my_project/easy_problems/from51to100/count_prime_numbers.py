import math

class Solution:
    def countPrimes(self, n: int) -> int:
        temp = 0
        if n == 0:
            return temp

        for i in range(1,n):
            if self.isPrime(i):
                temp += 1

        return temp

    def isPrime(self, num: int) -> bool:

        if num == 1:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False

        return True


solution = Solution()

print(solution.countPrimes(0))


