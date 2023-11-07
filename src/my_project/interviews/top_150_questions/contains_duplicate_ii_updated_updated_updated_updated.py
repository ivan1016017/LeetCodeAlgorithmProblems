from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        counts = defaultdict(int)

        len_nums = len(nums)

        for i in range(len_nums):
            counts[nums[i]] += 1
            if i > k:
                counts[nums[i-k-1]] -= 1
            if counts[nums[i]] > 1: 
                return True
            
        return False 