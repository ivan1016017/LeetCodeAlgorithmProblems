from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def hammingWeight(self, n: int) -> int: 
        return bin(n).count('1')
