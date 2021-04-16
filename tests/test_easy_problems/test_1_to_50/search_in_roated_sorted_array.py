from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        result = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return l
            else: l += 1
        return result

solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))