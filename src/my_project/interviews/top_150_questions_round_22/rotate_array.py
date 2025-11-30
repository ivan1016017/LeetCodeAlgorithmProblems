from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        len_nums = len(nums)
        k = k % len_nums

        nums[:] = nums[len_nums-k:] + nums[:len_nums-k]

        return nums
