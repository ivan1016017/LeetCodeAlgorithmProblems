from typing import List 

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        index: int = 0

        count: int = 0
        len_nums: int = len(nums)

        for i in range(len_nums):
            if nums[i] == 1:
                index = i 
                break 
        
        nums = nums[index:]
        len_nums = len(nums)

        for i in range(len_nums):
            if i == 0 and nums[i] == 1:
                continue
            if nums[i] == 0:
                count += 1
                
            else:
                
                if count < k:
                    return False 
                else: 
                    count = 0

        return True 


solution = Solution()

print(solution.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))

print(solution.kLengthApart(nums = [1,0,0,1,0,1], k = 2))

print(solution.kLengthApart(nums = [1,1,1,1,1], k = 0))

print(solution.kLengthApart(nums = [0,1,0,1], k = 1))
