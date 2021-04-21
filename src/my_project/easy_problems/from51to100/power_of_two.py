class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = True
        if n <= 0:
            return False
        if n == 1:
            return True
        if n > 1 and n % 2 == 1:
            return not result

        while n > 1:
            if n % 2 == 1:
                return False
            n = n // 2
        return result

solution = Solution()

print(solution.isPowerOfTwo(32))
