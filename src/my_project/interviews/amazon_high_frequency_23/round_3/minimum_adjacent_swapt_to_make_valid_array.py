from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        min_num = min(nums)
        max_num = max(nums)

        id_min  = nums.index(min_num)

        new_nums = [min_num] + nums[:id_min] + nums[id_min + 1:]

        id_max = new_nums[::-1].index(max_num)

        return id_min + id_max

