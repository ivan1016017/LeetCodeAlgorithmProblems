from typing import List
from collections import defaultdict

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        default_dict = defaultdict(int)
        count: int = 0
        solution: List[int] = list()

        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += 1

            default_dict[i] = count

        k_indices: List[int] = list()
        k_indices = list(default_dict.values())
        k_indices.sort()
        k_indices = k_indices[:k]

        for num in k_indices:
            for i, j in default_dict.items():
                if num == j and i not in solution:
                    solution.append(i)
                    break


        return solution

solution = Solution()
print(solution.kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))

print(solution.kWeakestRows( mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))