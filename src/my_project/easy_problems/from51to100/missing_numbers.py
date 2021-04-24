from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_list  = sorted(nums)

        for i in range(len(nums)+1):
            if i not in nums:
                return i







solution = Solution()
print(solution.missingNumber( [0,1]))
# this is the new comment to test git revert

# new comment added

# sample
