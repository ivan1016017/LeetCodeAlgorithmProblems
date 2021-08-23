from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        solution = []

        def func(i, j):
            if i >= 0 and i < m and j >= 0 and j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + func(i - 1, j) + func(i, j + 1) + func(i + 1, j) + func(i, j - 1)
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    solution.append(func(i, j))

        if solution:
            return max(solution)
        else:
            return 0