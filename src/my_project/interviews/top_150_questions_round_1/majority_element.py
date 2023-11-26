from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        sol_dict = dict()
        len_nums =len(nums)

        for i in range(len_nums):
            if nums[i] not in sol_dict:
                sol_dict[nums[i]] = 1
            else:
                sol_dict[nums[i]] += 1

        for i in range(len_nums):

            if sol_dict[nums[i]] > len_nums//2: 
                return nums[i]