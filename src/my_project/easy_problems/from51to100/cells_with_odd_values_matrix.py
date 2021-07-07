from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:


        # initialize variables
        solution = [[0 for y in range(n)] for x in range(m)]
        count = 0


        for item in indices:
            for j in range(n):
                solution[item[0]][j] += 1
            for i in range(m):
                solution[i][item[1]] += 1


        for i in range(m):
            for j in range(n):
                if solution[i][j] % 2 == 1:
                    count += 1



        return count

solution = Solution()
print(solution.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))

