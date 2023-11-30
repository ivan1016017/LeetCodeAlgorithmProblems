from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        else: 
            count = 0
            min_str, max_str = min(strs), max(strs)
            for i in range(len(min_str)):
                if min_str[i] != max_str[i]:
                    break
                else:
                    count += 1
            return min_str[:count]
