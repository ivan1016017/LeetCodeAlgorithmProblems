from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        window_start = 0
        min_size = float('inf')

        # summation of subarray
        sum_subarray = 0

        # use sliding windows to update min_size of valid subarray

        for window_end, num in enumerate(nums):

            sum_subarray += num 

            while sum_subarray >= target:

                # keep shrinking window size if sum_subarray is valid
                min_size = min(min_size, window_end-window_start+1)

                # update sum_subarray
                sum_subarray -= nums[window_start]
                window_start += 1

        if min_size == float('inf'):
            return 0
        else: 
            return min_size