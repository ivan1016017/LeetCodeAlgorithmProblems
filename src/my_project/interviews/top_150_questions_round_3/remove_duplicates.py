from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        len_nums = len(nums)

        for i in range(len_nums-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1 

        nums[j] = nums[len_nums-1] 

        return j + 1