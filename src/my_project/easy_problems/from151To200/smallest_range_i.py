from typing import List 

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, (max(nums)-k) - (min(nums)+k))

solution = Solution()

print(solution.smallestRangeI(nums = [1], k = 0))

print(solution.smallestRangeI(nums = [0,10], k = 2))

print(solution.smallestRangeI(nums = [1,3,6], k = 3))

print(solution.smallestRangeI(nums = [7,8,8], k = 5))

print(solution.smallestRangeI(nums = [3,1,10], k = 4))


