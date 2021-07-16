from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        # initialize variables
        count = 0

        for item in grid:
            for i in item:
                if i < 0:
                    count += 1
        return count


solution = Solution()
print(solution.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))