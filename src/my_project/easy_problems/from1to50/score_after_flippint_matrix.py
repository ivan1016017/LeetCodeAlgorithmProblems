from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:


        def count_ones(grid, col_number):
            row_len = len(grid)
            col_len = len(grid[0])
            count = 0
            for i in range(row_len):
                if grid[i][col_number] == 1:
                    count += 1

            return count

        def tog_row(grid, row_number):
            row = len(grid)
            col = len(grid[0])
            for j in range(col):
                if grid[row_number][j] == 1:
                    grid[row_number][j] = 0
                else:
                    grid[row_number][j] = 1

                return grid

        def tog_col(grid, col_number):
            row = len(grid)
            col = len(grid[0])
            for i in range(row):
                if grid[i][col_number] == 1:
                    grid[i][col_number] = 0
                else:
                    grid[i][col_number] = 1

            return grid

        def cal_number(grid):
            row = len(grid)
            col = len(grid[0])
            s = 0
            for i in range(row):
                for j in range(col):
                    s += grid[i][j] * 2**(col-j-1)
            return s

        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            if grid[i][0] == 0:
                grid = tog_row(grid,i)

        for j in range(1,col):

            cnt_1 = count_ones(grid, j )
            if cnt_1 < row/2:
                grid = tog_col(grid,j)

        return cal_number(grid)



solution = Solution()

print(solution.matrixScore(grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]))