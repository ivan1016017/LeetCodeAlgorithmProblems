from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # initialize variables
        rows = len(mat)
        columns = len(mat[0])
        dp = [[0 for y in range(columns)] for x in range(rows)]
        result = [[0 for y in range(columns)] for x in range(rows)]

        sum: int = 0
        for r in range(rows):
            for c in range(columns):
                sum = mat[r][c]
                if c > 0 :
                    sum += dp[r][c-1]
                if r > 0:
                    sum += dp[r-1][c]
                if r > 0 and c > 0:
                    sum -= dp[r-1][c-1]
                dp[r][c] = sum

        for r in range(rows):
            for c in range(columns):
                minr = max(0, r-k)
                minc = max(0, c-k)
                maxr = min(r+k, rows-1)
                maxc = min(c+k, columns-1)
                if minr >0 and minc >0:
                    result[r][c] = dp[maxr][maxc] + dp[minr-1][minc-1] - dp[minr-1][maxc] - dp[maxr][minc-1]
                elif minr > 0:
                    result[r][c] = dp[maxr][maxc] - dp[minr-1][maxc]
                elif minc > 0:
                    result[r][c] = dp[maxr][maxc] - dp[maxr][minc-1]
                else:
                    result[r][c] = dp[maxr][maxc]

        return result

solution = Solution()
print(solution.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1))