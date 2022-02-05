from typing import List 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        solution_dict = dict()
        
        for item in nums:
            
            if item not in solution_dict:
                solution_dict[item] = 0 

        for item in nums: 
            solution_dict[item] += 1
            if solution_dict[item] >=2:
                return item 
            
            
        
            
            
        