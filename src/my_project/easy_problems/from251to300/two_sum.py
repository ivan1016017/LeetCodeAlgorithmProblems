from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp_dict = dict()
        
        
        for index, value in enumerate(nums):
            if target - value in temp_dict:
                return temp_dict[target-value], index 
            
            temp_dict[value] = index
