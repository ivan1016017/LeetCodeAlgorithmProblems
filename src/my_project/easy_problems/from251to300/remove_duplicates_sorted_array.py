from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        len_nums = len(nums)
        
        if len_nums == 0 or len_nums == 1:
            return len_nums
        
        j = 0
        for i in range(len_nums-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j+=1
        nums[j] = nums[len_nums-1]
            
        return j + 1
                