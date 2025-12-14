from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If character seen before and in current window
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move left pointer past the last occurrence
                left = char_index[s[right]] + 1
            
            # Update last seen index of current character
            char_index[s[right]] = right
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length