from typing import List 

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        solution: int = 0

        x = len(grid)
        y = len(grid[0])
        for i in range(x):
            for j in range(y):
                if grid[i][j] != 0:
                    solution += 2 + grid[i][j]*4 
                    if i < x-1:
                        solution -= 2* min(grid[i][j], grid[i+1][j])
                    if j < y-1: 
                        solution -= 2* min(grid[i][j], grid[i][j+1])



        return solution


solution = Solution()


print(solution.surfaceArea(grid = [[2]]))

print(solution.surfaceArea(grid = [[1,2],[3,4]]))

print(solution.surfaceArea( grid = [[1,0],[0,2]]))

print(solution.surfaceArea( grid = [[1,1,1],[1,0,1],[1,1,1]]))

print(solution.surfaceArea( grid = [[2,2,2],[2,1,2],[2,2,2]]))

