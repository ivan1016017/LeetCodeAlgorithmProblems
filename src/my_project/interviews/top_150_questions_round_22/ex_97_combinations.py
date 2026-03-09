from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current: List[int]) -> None:
            # Base case: if we have k numbers, add to result
            if len(current) == k:
                result.append(current[:])
                return
            
            # Try all numbers from start to n
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(1, [])
        return result