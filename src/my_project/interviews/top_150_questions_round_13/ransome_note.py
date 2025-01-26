from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def canConstruct(self,ransomNote: str, magazine: str) -> bool:

        for s in set(ransomNote):

            if ransomNote.count(s) > magazine.count(s):
                return False 
            
        return True 