from typing import List 

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        

        flat_list = list()
        
        x = len(grid)
        y = len(grid[0])
        solution = list()
        for i in range(x):
            for j in range(y):
                flat_list.append(grid[i][j])
        temp = None
        for i in range(k):
            temp = flat_list.pop()
            flat_list = [temp] + flat_list

        for i in range(x):
            solution.append(flat_list[i*y: i*y +y])
        return solution

solution = Solution()

print(solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))

print(solution.shiftGrid( grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))

print(solution.shiftGrid( grid = [[13]], k = 4))


