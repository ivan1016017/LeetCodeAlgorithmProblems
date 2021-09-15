from typing import List 

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:


        projection_xy = 0
        projection_xz = 0
        projection_yz = 0

        for row in grid:
            projection_xy += sum([1 for x in row if x != 0])
            projection_xz += max(row)

        def max_column(grid, j):
            temp = list()
            for i in range(len(grid)):
                temp.append(grid[i][j])
            return max(temp)

        for j in range(len(grid[0])):
            projection_yz += max_column(grid, j)

        return projection_xy + projection_xz + projection_yz


solution = Solution()
print(solution.projectionArea(
[[1,0],[0,2]]))