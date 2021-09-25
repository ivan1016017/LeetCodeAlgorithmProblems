from typing import List 
from collections import defaultdict
import math 

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        temp_collections = defaultdict(int)
        for i in range(rows):
            for j in range(cols):
                temp_collections[(i,j)] = abs(i-rCenter) + abs(j-cCenter)

        l = [([k[0],k[1]],v) for k,v in temp_collections.items()]
        l.sort(key = lambda x: x[1])
        l = [item[0] for item in l]
        return l


solution = Solution()

print(solution.allCellsDistOrder( rows = 2, cols = 3, rCenter = 1, cCenter = 2))

print(solution.allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0))

print(solution.allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1))



