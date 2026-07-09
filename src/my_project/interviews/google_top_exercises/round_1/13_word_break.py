from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)

        # dp[i] is True if s[:i] can be segmented into dictionary words.
        # Empty prefix is trivially segmentable.
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # Try every split point j: s[:j] segmentable and s[j:i] a word.
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]