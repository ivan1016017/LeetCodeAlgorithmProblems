from typing import List 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        dp = [0]*(l+2)
        for i in range(3,l+2):
            dp[i] = min(dp[i-1]+cost[i-2],dp[i-2]+cost[i-3])
        return dp[l+1]