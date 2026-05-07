from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if we can jump from index 0 to the last index.
        
        Strategy: Greedy backward traversal
        - Work backwards from the end
        - Track the leftmost position that can reach the goal
        - If we can reach index 0, return True
        
        Time: O(n), Space: O(n) - can be optimized to O(1)
        """
        
        n = len(nums)

        # Base case: already at the end
        if n == 1: 
            return True 
        
        # dp[i] = 1 means position i can reach the end
        dp = [0] * n
        
        # Start from the last index (our goal)
        prev_best = n - 1
        step = n - 1

        # Iterate backwards from second-to-last to first index
        for i in range(n - 2, -1, -1):
            # Maximum jump length from current position
            step = nums[i]

            # Check if current position can reach any "good" position
            # (i + step) is the farthest we can jump from position i
            if (i + step) >= prev_best:
                # Mark this position as reachable to the end
                dp[i] = 1
                
                # Update the leftmost position that can reach the end
                prev_best = i

        # Check if we can reach the end from the start (index 0)
        if dp[0]:
            return True 
        
        return False