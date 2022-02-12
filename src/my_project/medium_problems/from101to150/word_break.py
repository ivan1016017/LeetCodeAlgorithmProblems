from typing import List, Optional 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        print(d)
        return d[-1]
    
solution = Solution()

print(solution.wordBreak(s = "leetcode", wordDict = ["leet","code"]))