from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        l1, l2 = 0, 0 

        len_s, len_t = len(s), len(t)

        while l1 < len_s and l2 < len_t:

            if s[l1] == t[l2]:
                l1 += 1

            l2 += 1

        return l1 == len_s