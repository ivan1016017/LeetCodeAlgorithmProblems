from typing import List 

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        answer = 0
        sumAlongCol = 0
        for i in range(len(mat)):
            if (sum(mat[i])) !=1:
                continue 
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    continue 
                else: 
                    sumAlongCol = 0
                    for k in range(len(mat)):
                        sumAlongCol += mat[k][j]
                    if sumAlongCol == 1:
                        answer += 1

        return answer 


solution = Solution()

print(solution.numSpecial(mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]))

print(solution.numSpecial( mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]))

print(solution.numSpecial(mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]))
