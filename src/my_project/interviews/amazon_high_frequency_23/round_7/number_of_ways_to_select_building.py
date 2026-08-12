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
        total_zeros = s.count('0')
        total_ones = len(s) - total_zeros

        left_zeros = left_ones = 0
        ways = 0

        for ch in s:
            if ch == '1':
                # middle is '1' -> need '0' on both sides -> "010"
                right_zeros = total_zeros - left_zeros
                ways += left_zeros * right_zeros
                left_ones += 1
            else:  # ch == '0'
                # middle is '0' -> need '1' on both sides -> "101"
                right_ones = total_ones - left_ones
                ways += left_ones * right_ones
                left_zeros += 1

        return ways