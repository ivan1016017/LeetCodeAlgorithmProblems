from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max1 = list()
        max2 = list()
        ops = 0

        for i in grid:
            max1.append(max(i))

        for j in map(list, zip(*grid)):
            max2.append(max(j))

        for i1, val1 in enumerate(max1):
            for i2, val2 in enumerate(max2):
                ops += (min(val1, val2) - grid[i1][i2])

        return ops


solution = Solution()
print(solution.maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))