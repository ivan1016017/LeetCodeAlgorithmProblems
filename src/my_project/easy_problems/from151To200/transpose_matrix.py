from typing import List 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        flat_matrix = list()
        x = len(matrix)
        y = len(matrix[0])

        for j in range(y):
            for i in range(x):
                flat_matrix.append(matrix[i][j])

        transpose_matrix = list()

        for i in range(y):
            transpose_matrix.append(flat_matrix[i*x:i*x + x])


        return transpose_matrix

solution = Solution()

print(solution.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))

print(solution.transpose(matrix = [[1,2,3],[4,5,6]]))


# function to be reverted 

def functionToBeReverted(num: int)-> int:
    return num *7
