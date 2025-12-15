from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # Frequency map of characters needed from t
        t_freq = Counter(t)
        required = len(t_freq)  # Number of unique characters in t
        
        # Window character frequencies
        window_freq = {}
        
        # Track how many unique characters in window have desired frequency
        formed = 0
        
        # Left and right pointers
        left = 0
        min_len = float('inf')
        min_left = 0
        
        for right in range(len(s)):
            # Add character from right to window
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1
            
            # Check if frequency of current character matches desired frequency
            if char in t_freq and window_freq[char] == t_freq[char]:
                formed += 1
            
            # Try to contract window until it's no longer valid
            while left <= right and formed == required:
                # Update result if current window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Remove leftmost character from window
                left_char = s[left]
                window_freq[left_char] -= 1
                
                # Check if window is no longer valid
                if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]