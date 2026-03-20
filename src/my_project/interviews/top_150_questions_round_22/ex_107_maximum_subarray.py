from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        local_maximum = 0
        global_maximum = -(10**10)

        for i in range(n):

            local_maximum = max(nums[i], nums[i]+local_maximum)
            
            if local_maximum > global_maximum:
                global_maximum = local_maximum

        return global_maximum

