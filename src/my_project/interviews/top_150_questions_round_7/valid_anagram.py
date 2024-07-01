from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        lst_s = [c for c in s]
        lst_t = [c for c in t]

        lst_s.sort()
        lst_t.sort()

        return ''.join(lst_s) == ''.join(lst_t)
