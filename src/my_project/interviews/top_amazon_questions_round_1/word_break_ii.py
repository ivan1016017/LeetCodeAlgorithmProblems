from typing import List, Union

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordSet = set(wordDict)

        def helper(i, cur, path):
            if i == len(s):
                if not cur:
                    res.append(' '.join(path))
                return
            
            cur += s[i]  # include current character
            
            if cur in wordSet:
                helper(i + 1, '', path + [cur])  # cut here

            helper(i + 1, cur, path)  # continue building cur

        helper(0, '', [])
        return res