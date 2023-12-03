from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # set initial value
        len_s, len_t = len(s), len(t)
        c_s, c_t = 0, 0
        # count num of indeces in which s and t are the same
        while c_s < len_s and c_t < len_t: 
            if s[c_s] == t[c_t]:
                c_s += 1
            c_t += 1
        # validate if s is substring of t
        return c_s == len_s 