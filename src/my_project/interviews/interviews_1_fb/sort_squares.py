from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = [x**2 for x in nums]
        temp.sort()
        return temp
