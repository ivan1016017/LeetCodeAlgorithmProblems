from typing import List

class SecondSolution:
    def buildArray(self, nums: List[int]) -> List[int]:

        # initialize variables
        len_nums = len(nums)
        solution = list()

        for i in range(len_nums):
            solution.append(nums[nums[i]])

        return solution


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        # initialize variables
        len_nums = len(nums)
        solution = [0 for x in range(len_nums)]

        for i in range(len_nums):
            solution[i] = nums[nums[i]]

        return solution


solution = Solution()
print(solution.buildArray(nums = [0,2,1,5,3,4]))