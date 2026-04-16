from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Dynamic Programming approach:
        - For each house, we choose max of:
          1. Rob current house + max money from i-2 houses
          2. Skip current house and take max money from i-1 houses
        
        Time: O(n), Space: O(1)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # prev2: max money robbed up to i-2
        # prev1: max money robbed up to i-1
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = current
        
        return prev1