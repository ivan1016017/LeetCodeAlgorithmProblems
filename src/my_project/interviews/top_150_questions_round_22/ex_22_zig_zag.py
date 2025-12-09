from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Alternative implementation with detailed comments.
        """
        
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Process each character
        for char in s:
            # Append character to current row
            rows[current_row] += char
            
            # At boundaries, reverse direction
            # - At row 0 (top): start going down
            # - At row numRows-1 (bottom): start going up
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Update current row based on direction
            # going_down=True: increment row (1, 2, 3...)
            # going_down=False: decrement row (...3, 2, 1)
            current_row += 1 if going_down else -1
        
        # Join all rows into final result
        return ''.join(rows)