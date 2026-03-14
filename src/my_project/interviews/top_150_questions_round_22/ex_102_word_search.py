from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Search for a word in a 2D board using backtracking.
        
        Time Complexity: O(m * n * 4^L) where m, n are board dimensions and L is word length
        Space Complexity: O(L) for recursion stack
        """
        if not board or not board[0] or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(row: int, col: int, index: int) -> bool:
            # Base case: found all characters
            if index == len(word):
                return True
            
            # Check boundaries and character match
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                board[row][col] != word[index]):
                return False
            
            # Mark cell as visited by temporarily changing it
            temp = board[row][col]
            board[row][col] = '#'
            
            # Explore all 4 directions
            found = (dfs(row + 1, col, index + 1) or
                    dfs(row - 1, col, index + 1) or
                    dfs(row, col + 1, index + 1) or
                    dfs(row, col - 1, index + 1))
            
            # Backtrack: restore the cell
            board[row][col] = temp
            
            return found
        
        # Try starting from each cell
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False