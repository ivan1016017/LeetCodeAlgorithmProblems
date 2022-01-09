from typing import List 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums: 
            return 0 
        
        len_nums: int = len(nums)
        dp = [1]*len_nums
        
        for i in range(1,len_nums):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
                
        
        return max(dp)