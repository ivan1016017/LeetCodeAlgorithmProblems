from functools import lru_cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(left, right):
            if left > right: return (0, 0)

            pickLeft = dp(left + 1, right)
            pickRight = dp(left, right - 1)

            if piles[left] + pickLeft[1] > piles[right] + pickRight[
                1]:  # If the left choice has higher score than the right choice
                return piles[left] + pickLeft[1], pickLeft[0]  # then pick left

            return piles[right] + pickRight[1], pickRight[0]  # else pick right

        alexScore, leeScore = dp(0, len(piles) - 1)
        return alexScore > leeScore

class SecondSolution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        def helper(i,j,alex,lee):
            if i>j:
                return alex>lee
            return helper(i+1,j-1,alex+piles[i],lee+piles[j]) or helper(i+1,j-1,alex+piles[j],lee+piles[i])
        return helper(0,n-1,0,0)