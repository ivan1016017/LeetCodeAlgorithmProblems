from typing import List, Union, Collection, Mapping, Optional   
from abc import ABC, abstractmethod

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ord_index = {c:i for i, c in enumerate(order)}

        for a,b in zip(words,words[1:]):
            if len(a) > len(b) and a[:len(b)]==b:
                return False 
            for s1, s2 in zip(a,b):
                if ord_index[s1] < ord_index[s2]:
                    break 
                elif ord_index[s1] > ord_index[s2]:
                    return False 
        return True 
        