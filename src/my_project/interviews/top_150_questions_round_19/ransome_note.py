from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def canConstruct(self,ransomNote: str, magazine: str) -> bool:

        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False 
            
        return True