from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        Count valid 3-building selections forming "010" or "101" patterns.
        
        Key insight: Track how many 2-character patterns we can form,
        then extend them with the appropriate third character.
        
        Time: O(n), Space: O(1)
        """

        count_0 = 0  # Count of '0' seen so far
        count_1 = 0  # Count of '1' seen so far
        count_01 = 0  # Count of "01" patterns (0 followed by 1)
        count_10 = 0  # Count of "10" patterns (1 followed by 0)
        
        result = 0
        
        for char in s:
            if char == '0':
                # Current '0' can complete "010": we need "01" before this '0'
                result += count_01
                
                # Current '0' can start new "01" patterns: pair with each previous '0'
                # Wait no, "01" means 0 then 1, so we can't create "01" with another 0
                
                # Current '0' extends all previous '1' to form "10" pattern
                count_10 += count_1
                
                count_0 += 1
            else:  # char == '1'
                # Current '1' can complete "101": we need "10" before this '1'
                result += count_10
                
                # Current '1' extends all previous '0' to form "01" pattern
                count_01 += count_0
                
                count_1 += 1
        
        return result

