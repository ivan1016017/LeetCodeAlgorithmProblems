from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of distinct integers.
        
        Approach: Backtracking
        - Use recursion to build permutations
        - At each step, try adding each unused number
        - When current permutation is complete, add to results
        - Backtrack and try other possibilities
        
        Time Complexity: O(n! * n) - n! permutations, each takes O(n) to build
        Space Complexity: O(n) - recursion depth + current permutation
        """
        result = []
        
        def backtrack(current: List[int], remaining: List[int]):
            # Base case: no more numbers to add
            if not remaining:
                result.append(current[:])
                return
            
            # Try each remaining number as the next element
            for i in range(len(remaining)):
                # Choose: add remaining[i] to current permutation
                current.append(remaining[i])
                # Explore: recurse with remaining numbers
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(current, new_remaining)
                # Unchoose: backtrack
                current.pop()
        
        backtrack([], nums)
        return result