from typing import List 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        nums.sort(reverse=True)
        
        
        
        return nums[k-1] 
    
solution = Solution()

print(solution.findKthLargest([1,2,3,4,5],4))