from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate product of all elements except self without division.
        
        Strategy: Two-pass with prefix and suffix products
        - First pass: Build prefix products (product of all elements to the left)
        - Second pass: Build suffix products (product of all elements to the right)
        - Result[i] = prefix[i] * suffix[i]
        
        Optimization: Use output array to store prefix, then multiply by suffix in-place
        
        Time: O(n), Space: O(1) excluding output array
        """
        
        n = len(nums)
        answer = [1] * n
        
        # First pass: Calculate prefix products
        # answer[i] contains product of all elements to the left of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Second pass: Calculate suffix products and multiply with prefix
        # For each position, multiply existing prefix with product of all elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer