from typing import List 
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        m = collections.defaultdict(list)
        for s in strs:
            m["".join(sorted(s))].append(s)
        return [v for v in m.values()]
    
    
a = 'cba'
b = sorted(a)
print(b)