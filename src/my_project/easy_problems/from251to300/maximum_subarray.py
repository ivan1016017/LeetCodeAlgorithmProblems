from threading import local
from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        local_max = 0
        global_max = - (10**10)
        
        for i in range(n):
            local_max = max(nums[i], local_max+nums[i])
            
            if local_max > global_max:
                global_max = local_max
                
        return global_max