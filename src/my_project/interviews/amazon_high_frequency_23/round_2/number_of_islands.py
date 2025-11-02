from typing import List, Union, Collection, Mapping, Optional
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """BFS approach - explores island level by level"""

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r: int, c: int):
            queue = deque([(r,c)])
            grid[r][c] = '0'

            while queue: 
                row, col = queue.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1'):
                        grid[nr][nc] = '0'
                        queue.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r,c)

        return islands
    

    def numIslands_DFS(grid: List[List[str]]) -> int:
        """DFS approach - explores island depth-first"""

        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'):
                return 
            
            grid[r][c] = '0' 

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)

        return islands

