from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Convert to set for O(1) lookup
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            # (i.e., num - 1 is not in the set)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
        