from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        len_column = len(mat)

        for i in range(len_column):
            count += mat[i][i] + mat[i][len_column - 1 - i]



        if len_column % 2 == 1:
            i = (len_column // 2)
            count -= mat[i][i]
        return count

solution = Solution()
print(solution.diagonalSum(mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))