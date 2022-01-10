from typing import List 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1)+1, len(word2)+1
        dp = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n + m - 2 - 2*dp[-1][-1]