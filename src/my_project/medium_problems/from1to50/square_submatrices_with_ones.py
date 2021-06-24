from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        # initialize variable
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for y in range(n)] for x in range(m)]
        temp = 0

        for i in range(m):
            dp[i][0] = matrix[i][0]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1], dp[i-1][j])

        for i in range(m):
            for j in range(n):
                temp += dp[i][j]
        return temp


solution = Solution()
print(solution.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))