from typing import List 

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        if len(mat)*len(mat[0]) != r*c:
            return mat 

        solution_matrix = list()
        flat_list = list()

        for row in mat:
            for num in row:
                flat_list.append(num)
        k = 0
        for i in range(r):
            solution_matrix.append(flat_list[k:c+k])
            k+=c
                
        

        return solution_matrix

solution = Solution()

print(solution.matrixReshape( mat = [[1,2],[3,4]], r = 1, c = 4))

print(solution.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))

