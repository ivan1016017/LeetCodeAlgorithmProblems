from typing import List 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        le=len(nums)
        l=[0]*(le)
        for i in range(2,le):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                l[i]=1+l[i-1]
        return sum(l)