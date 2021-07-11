from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        # initialize variables
        count: int = 0
        for item in nums:
            if len(str(item))%2 == 0:
                count += 1
        return count

solution = Solution()
print(solution.findNumbers(nums = [12,345,2,6,7896]))