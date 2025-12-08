from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''
        
        min_strs, max_strs = min(strs), max(strs)
        count = 0

        for i in range(len(min_strs)):

            if min_strs[i] == max_strs[i]:
                count  += 1
            else: 
                break

        return min_strs[:count]