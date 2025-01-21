from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        lst_s = s.split()

        return len(lst_s[-1])

