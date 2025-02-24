from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic_answer = dict()
        len_nums = len(nums)

        for i in range(len_nums):

            if nums[i] not in dic_answer:
                dic_answer[nums[i]] = 1
            else:
                dic_answer[nums[i]] += 1

            if dic_answer[nums[i]] > len_nums//2:
                return nums[i]
            else:
                pass 

        return -1
