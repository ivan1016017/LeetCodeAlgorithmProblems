
class Solution:
    def addDigits(self, num: int) -> int:
        if num % 9 == 0:
            return 9

        return num % 9



solution = Solution()

print(solution.addDigits(38))