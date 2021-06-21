import collections
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # initialize variables
        len_nums = len(nums)
        temp = 0
        temp_solution = [0 for x in range(len_nums)]
        for i in range(len_nums):
            temp = 0
            for j in range(i+1, len_nums):
                if nums[i] > nums[j]:
                    temp_solution[i] += 1
                elif nums[i] < nums[j]:
                    temp_solution[j] += 1



        return temp_solution

solution = Solution()

print(solution.smallerNumbersThanCurrent([7,7,7,7]))

d = collections.defaultdict(list)
print(d)


class SecondSolution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        my_list = sorted(nums)
        dict = {}
        dict[my_list[0]] = 0

        for i in range(1, len(my_list)):
            if my_list[i] > my_list[i - 1]:
                dict[my_list[i]] = i
            else:
                dict[my_list[i]] = dict[my_list[i - 1]]

        for j in range(len(nums)):
            my_list[j] = dict[nums[j]]

        return my_list