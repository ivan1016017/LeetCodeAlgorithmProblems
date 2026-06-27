from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        answer = 0
        dp = {0:1}
        acc = 0

        for num in nums:
            acc += num
            answer += dp.get(acc - k, 0)
            dp[acc] = dp.get(acc, 0) + 1

        return answer 