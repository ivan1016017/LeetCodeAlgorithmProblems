from typing import List 

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count: int = 0
        
        len_pref = len(pref)
        
        for word in words:
            if word[0:len_pref] == pref:
                count += 1
        
        
        return count