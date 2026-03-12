from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Given an integer n, return the number of distinct solutions to the n-queens puzzle.
        
        The n-queens puzzle is placing n queens on an n×n chessboard such that
        no two queens attack each other (same row, column, or diagonal).
        
        Time Complexity: O(N!)
        Space Complexity: O(N)
        """
        def backtrack(row: int) -> int:
            # Base case: all queens placed successfully
            if row == n:
                return 1
            
            count = 0
            # Try placing queen in each column of current row
            for col in range(n):
                # Calculate diagonal and anti-diagonal identifiers
                diagonal = row - col
                anti_diagonal = row + col
                
                # Check if current position is safe
                if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue
                
                # Place queen
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)
                
                # Recurse to next row
                count += backtrack(row + 1)
                
                # Backtrack: remove queen
                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)
            
            return count
        
        # Track occupied columns, diagonals, and anti-diagonals
        cols = set()
        diagonals = set()  # row - col is constant for each diagonal
        anti_diagonals = set()  # row + col is constant for each anti-diagonal
        
        return backtrack(0)