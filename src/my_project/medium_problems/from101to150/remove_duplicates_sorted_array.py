from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        i = 0
        count = 1
        flag = False 
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                if not flag: 
                    flag = True
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    count += 1
            else:
                flag = False
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
        return count
        
        
