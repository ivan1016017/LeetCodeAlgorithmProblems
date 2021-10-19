from typing import List 

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        len_nums: int = len(nums)
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:len_nums]):
                return i
        if len_nums == 2:
            return -1
        if len_nums == 1:
            return 0

        return -1

solution = Solution()

print(solution.findMiddleIndex(nums = [2,3,-1,8,4]))

print(solution.findMiddleIndex(nums = [1,-1,4]))

print(solution.findMiddleIndex(nums = [2,5]))

print(solution.findMiddleIndex(nums = [1]))


        