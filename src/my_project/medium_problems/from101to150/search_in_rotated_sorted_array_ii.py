from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        return target in nums
    
    
class SolutionTwo:
    def search(self, nums: List[int], target: int) -> bool:
        
        flag: str = False 
        
        for num in nums:
            if num == target:
                return not flag
        
        
        return flag