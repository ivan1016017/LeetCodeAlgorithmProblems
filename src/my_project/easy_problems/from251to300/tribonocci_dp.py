class Solution:
    def tribonacci(self, n: int) -> int:
        if(n == 0): return 0
        dp = [0,1,1] + [0] * (n-2)
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]