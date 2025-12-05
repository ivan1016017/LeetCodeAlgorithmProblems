from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate how much water can be trapped after raining.
        
        Key insight: Water trapped at position i = min(max_left, max_right) - height[i]
        (if positive)
        
        Strategy: Two-pointer approach
        - Use two pointers from both ends
        - Track max height seen from left and right
        - Move pointer with smaller max height (water level determined by shorter side)
        - Add water trapped at current position
        
        Time: O(n), Space: O(1)
        """
        
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        
        while left < right:
            # Update max heights seen so far
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # Water level is determined by the shorter side
            if left_max < right_max:
                # Left side is shorter, so water trapped at left position
                # is determined by left_max
                water_trapped += left_max - height[left]
                left += 1
            else:
                # Right side is shorter or equal, so water trapped at right position
                # is determined by right_max
                water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped
