from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is less than next element, peak must be on the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Otherwise, peak is on the left (including mid)
                right = mid
        
        return left