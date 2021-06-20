from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # initialize variables
        len_nums = len(nums)
        temp = 0
        # loop through the array and find good pairs
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                if nums[i] == nums[j]:
                    temp += 1

        return temp


solution = Solution()
print(solution.numIdenticalPairs([1,2,3,1,1,3]))


