from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses.
        
        Uses backtracking approach:
        - Only add '(' if we haven't used all n openings
        - Only add ')' if closing count < opening count
        - When length = 2*n, we have a valid combination
        
        Time: O(4^n / sqrt(n)) - Catalan number
        Space: O(n) for recursion depth
        """
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: we've used all n pairs
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add opening parenthesis if we haven't used all n
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add closing parenthesis if it doesn't exceed opening count
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result