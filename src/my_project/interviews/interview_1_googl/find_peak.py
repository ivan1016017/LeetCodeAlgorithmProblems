from typing import List, Union, Mapping, Collection, Optional
from abc import ABC, abstractmethod

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i+j) // 2
            if nums[mid] > nums[mid+1]:
                j = mid
            else:
                i = mid+1
        return i