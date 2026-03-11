from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current: List[int], remaining: int):
            # Base case: found a valid combination
            if remaining == 0:
                result.append(current[:])
                return
            
            # Base case: exceeded target
            if remaining < 0:
                return
            
            # Explore all candidates starting from 'start' index
            for i in range(start, len(candidates)):
                # Include candidates[i] in the current combination
                current.append(candidates[i])
                
                # Recurse with the same start index (we can reuse the same number)
                backtrack(i, current, remaining - candidates[i])
                
                # Backtrack: remove the last added element
                current.pop()
        
        backtrack(0, [], target)
        return result
        