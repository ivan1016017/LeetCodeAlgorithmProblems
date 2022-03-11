from functools import lru_cache
from typing import List 

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        m, n = len(s), len(t)
        
        @lru_cache(None)
        def dp(i, j, k):
            # base cases
            if i < 0 or j < 0 or k < 0:
                return 0
            if k == 0 and s[i] != t[j]:
                return 0
            
            # dp transition
            ans = 0
            if s[i] == t[j]:
                ans += dp(i-1, j-1, k) + (k == 0)
            else:
                ans += dp(i-1, j-1, k-1) + 1
            
            return ans
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dp(i, j, 1)
        return ans