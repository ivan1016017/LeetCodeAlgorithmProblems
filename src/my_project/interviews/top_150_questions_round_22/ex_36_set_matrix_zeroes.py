from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Flags to track if first row/column should be zeroed
        first_row_zero = False
        first_col_zero = False
        
        # Check if first row has any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Check if first column has any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Use first row and column as markers
        # Check rest of matrix and mark first row/column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column
        
        # Set zeros based on markers (skip first row/column)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix