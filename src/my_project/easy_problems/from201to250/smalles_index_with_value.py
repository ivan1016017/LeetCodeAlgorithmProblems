from typing import List 

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        solution: int = -1
        len_nums: int = len(nums)
        for i in range(len_nums):
            if nums[i] == i %10:
                solution = i 
                return solution 
        return solution 



solution = Solution()

print(solution.smallestEqual(nums = [0,1,2]))

print(solution.smallestEqual(nums = [4,3,2,1]))

print(solution.smallestEqual(nums = [1,2,3,4,5,6,7,8,9,0]))

print(solution.smallestEqual(nums = [2,1,3,5,2]))
