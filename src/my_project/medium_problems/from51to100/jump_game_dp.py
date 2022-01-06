from typing import List 

class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if n==1:
            return True
        
        dp = [0]*(n)
        
        prev_best = n-1
        
        dp[n-1] = 1
        
        for i in range(n-2, -1, -1):
            
            step = nums[i]
            
            if (i+step)>=prev_best:
                
                dp[i] = 1
                prev_best = i
        
        
        if dp[0]:
            return True
        
        return False