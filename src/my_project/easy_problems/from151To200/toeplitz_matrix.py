from typing import List
from typing import List 

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        answer: bool = True

        if len(matrix) ==1 or len(matrix[0]) ==1:
            return answer
        for i in range(1,len(matrix)):
            
            for j in range(1,len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    answer = False 
                    return answer 

        return answer


solution = Solution()

print(solution.isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

print(solution.isToeplitzMatrix(matrix = [[1,2],[2,2]]))

print(solution.isToeplitzMatrix(matrix = [[18],[66]]))

print(solution.isToeplitzMatrix(matrix = [[11,74,0,93],[40,11,74,7]]))




