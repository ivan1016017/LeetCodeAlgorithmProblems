import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n: int = len(s)
        st: int = 0
        mx: int = 1
        bool_matrix  = [[None for x in range (n)] for y in range(n)]

        for i in range(n):
            bool_matrix[i][i] = True
            for l in range(2,n+1):
                print(3)

        return bool_matrix

solution = Solution()
print(solution.longestPalindrome("1234"))
