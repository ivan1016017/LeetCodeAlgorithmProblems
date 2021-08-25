from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:

        max_number: int = max(nums)
        min_number: int = min(nums)

        solution = None
        for number in range(1, min_number + 1):
            if max_number % number == 0 and min_number % number == 0:
                solution = number

        return solution


solution = Solution()

print(solution.findGCD(nums = [7,5,6,8,3]))