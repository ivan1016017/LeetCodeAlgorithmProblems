from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        list_s = s.split()
        
        return len(list_s[-1])