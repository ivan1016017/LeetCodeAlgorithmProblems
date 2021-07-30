from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        # initialize variables
        m = len(rowSum)
        n = len(colSum)
        solution = [[0 for y in range(n)] for x in range(m)]

        def fill_values(rows,cols):
            if rows == m or cols == n:
                return


            solution[rows][cols] = min(rowSum[rows], colSum[cols])

            if solution[rows][cols] == rowSum[rows]:
                colSum[cols] -= rowSum[rows]
                fill_values(rows +1, cols)
            else:
                rowSum[rows] -= colSum[cols]
                fill_values(rows, cols+1)

        fill_values(0,0)



        return solution

solution = Solution()
print(solution.restoreMatrix(rowSum = [3,8], colSum = [4,7]))