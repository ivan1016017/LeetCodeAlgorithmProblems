from typing import List
from collections import defaultdict

class SecondSolution:
    def sumOfUnique(self, nums: List[int]) -> int:

        # initialize variables
        count_dict = defaultdict(list)
        len_nums: int = len(nums)
        solution: int = 0

        for i in range(len_nums):
            count_dict[nums[i]].append(1)

        for i in count_dict.keys():
            if len(count_dict[i]) == 1:
                solution += i

        return solution

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        # initialize variables
        count_dict: dict = dict()
        len_nums: int = len(nums)
        solution: int = 0

        for i in range(len_nums):
            count_dict[nums[i]] = 0

        for i in range(len_nums):
            count_dict[nums[i]] += 1

        for i in count_dict.keys():
            if count_dict[i] == 1:
                solution += i

        return solution





solution = Solution()
print(solution.sumOfUnique(nums = [1,2,3,2]))

print(solution.sumOfUnique(nums = [1,1,1,1,1]))