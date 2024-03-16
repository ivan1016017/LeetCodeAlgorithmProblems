from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_needle = len(needle)
        len_haystack = len(haystack)

        for i in range(len_haystack-len_needle+1):

            if haystack[i:i+len_needle] == needle: 
                return i
            
        return -1
            

