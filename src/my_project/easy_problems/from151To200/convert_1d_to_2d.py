from typing import List 

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        len_original: int = len(original)
        solution = list()
        temp = list()
        if len_original != m*n:
            return [[]]
        else: 
            for i in range(m):
                temp = list()
                for j in range(n):
                    temp.append(original[j + i*n])
                solution.append(temp)
            return solution

solution = Solution()

print(solution.construct2DArray(original = [1,2,3,4], m = 2, n = 2))

print(solution.construct2DArray(original = [1,2,3], m = 1, n = 3))

print(solution.construct2DArray(original = [1,2], m = 1, n = 1))

print(solution.construct2DArray(original = [3], m = 1, n = 2))

