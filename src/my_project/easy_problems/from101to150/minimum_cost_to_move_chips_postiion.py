from typing import List 

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        even_count: int = 0
        odd_count: int = 0
        for val in position:
            if val % 2 == 0:
                even_count += 1

            else: 
                odd_count += 1 

                
        return min(even_count, odd_count)


solution = Solution()

print(solution.minCostToMoveChips(position = [2,2,2,3,3]))
