from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: 
            return ''
        else:
            min_strs, max_strs = min(strs), max(strs)
            count = 0

            len_min_strs = len(min_strs)

            for i in range(len_min_strs):
                if min_strs[i] != max_strs[i]:
                    break 
                else:
                    count += 1

            return min_strs[:count]
