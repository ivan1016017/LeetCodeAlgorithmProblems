from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [row[:] for row in grid]
        for i in range(1, m):
            dp[i][0] += dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]
