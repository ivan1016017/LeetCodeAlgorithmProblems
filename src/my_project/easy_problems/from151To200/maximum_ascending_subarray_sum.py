from typing import List 

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        temp_max: int = nums[0]
        count: int = 0
        min_index: int  = 0
        max_index: int = 0

        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                max_index = i
                if sum(nums[min_index:max_index+1]) > temp_max:
                    temp_max = sum(nums[min_index:max_index+1])
            else: 
                min_index = i
                max_index = i
        return temp_max

solution = Solution()

print(solution.maxAscendingSum(nums = [10,20,30,5,10,50]))

print(solution.maxAscendingSum(nums = [10,20,30,40,50]))

print(solution.maxAscendingSum(nums = [12,17,15,13,10,11,12]))

print(solution.maxAscendingSum(nums = [100,10,1]))

