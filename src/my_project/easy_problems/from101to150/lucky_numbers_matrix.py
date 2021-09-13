from typing import List 

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        solution: List[int] = list()

        def getColumn(matrix, j):
            my_slide: List[int] = list()
            for i in range(len(matrix)):
                my_slide.append(matrix[i][j])
            return my_slide 

            return None 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print( min([x for x in matrix[i][:]]) ,   max(getColumn(matrix, j)))
                # print(matrix[i][j])
                if matrix[i][j] == min([x for x in matrix[i][:]]) and matrix[i][j] == max(getColumn(matrix, j)): 
                    solution.append(matrix[i][j])
        return solution



solution = Solution()

print(solution.luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))




