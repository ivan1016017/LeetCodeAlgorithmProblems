from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # BFS to mark all 'O's connected to border
        def bfs(row: int, col: int) -> None:
            queue = deque([(row, col)])
            board[row][col] = 'T'  # Temporary marker for safe 'O's
            
            while queue:
                r, c = queue.popleft()
                # Check all 4 directions
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                        board[nr][nc] = 'T'
                        queue.append((nr, nc))
        
        # Step 1: Mark all border-connected 'O's
        # Check first and last row
        for col in range(n):
            if board[0][col] == 'O':
                bfs(0, col)
            if board[m-1][col] == 'O':
                bfs(m-1, col)
        
        # Check first and last column
        for row in range(m):
            if board[row][0] == 'O':
                bfs(row, 0)
            if board[row][n-1] == 'O':
                bfs(row, n-1)
        
        # Step 2: Flip all remaining 'O's to 'X' and restore 'T' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Surrounded region
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # Border-connected, restore