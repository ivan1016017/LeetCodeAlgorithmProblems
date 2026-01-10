from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))