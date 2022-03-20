from typing import List 

class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        
        min_num: int = min(nums)
        max_num: int = max(nums)
        
        count = 0
        
        for num in nums:
            if num > min_num and num < max_num:
                count += 1
            
            
            
        
        return count
    
    
solution = Solution()

print(solution.countElements([11,7,2,15]))

print(solution.countElements([-3,3,3,90]))


