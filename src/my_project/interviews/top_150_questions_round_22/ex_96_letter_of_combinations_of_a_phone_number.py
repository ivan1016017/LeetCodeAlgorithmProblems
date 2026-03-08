from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current: str):
            # Base case: if we've processed all digits
            if index == len(digits):
                result.append(current)
                return
            
            # Get the letters for the current digit
            letters = phone_map[digits[index]]
            
            # Try each letter and recurse
            for letter in letters:
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return result
        