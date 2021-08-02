from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        # initialize
        piles.sort()
        solution: list[int] = list()
        len_piles: int = len(piles)
        count: int = 0

        for i in range(len_piles-2, 0,-2):
            solution.append(piles[i])
            count += 1
            if count == len_piles//3:
                break


        return sum(solution)

solution = Solution()
print(solution.maxCoins(piles = [2,4,5]))

