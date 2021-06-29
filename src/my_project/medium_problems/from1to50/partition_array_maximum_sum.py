from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for _ in range(len(arr))]
        maximum = 0
        for i in range(k):
            maximum = max(arr[i], maximum)
            dp[i] = maximum * (i + 1)
        print(dp)

        for i in range(k, len(arr)):
            maximum = arr[i]
            for j in range(k):
                maximum = max(maximum, arr[i - j])
                dp[i] = max(dp[i], dp[i - j - 1] + maximum * (j + 1))

        return dp[-1]

solution = Solution()
solution.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3)