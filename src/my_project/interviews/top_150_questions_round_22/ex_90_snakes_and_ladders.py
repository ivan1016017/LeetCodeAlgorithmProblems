from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Helper function to convert square number to (row, col) coordinates
        def get_position(square):
            # square is 1-indexed, convert to 0-indexed
            square -= 1
            # Calculate row from bottom (0 is bottom row)
            row = square // n
            # Calculate column based on row direction
            if row % 2 == 0:
                # Even rows (from bottom): left to right
                col = square % n
            else:
                # Odd rows (from bottom): right to left
                col = n - 1 - (square % n)
            # Convert to board coordinates (0 is top row in board)
            return n - 1 - row, col
        
        # BFS to find shortest path
        target = n * n
        queue = deque([(1, 0)])  # (current_square, num_moves)
        visited = {1}
        
        while queue:
            curr, moves = queue.popleft()
            
            # Try all possible dice rolls (1 to 6)
            for dice in range(1, 7):
                next_square = curr + dice
                
                # Check if we've gone beyond the board
                if next_square > target:
                    break
                
                # Get the board position for this square
                r, c = get_position(next_square)
                
                # Check if there's a snake or ladder
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                # Check if we've reached the target
                if next_square == target:
                    return moves + 1
                
                # Add to queue if not visited
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        # If we can't reach the target
        return -1


