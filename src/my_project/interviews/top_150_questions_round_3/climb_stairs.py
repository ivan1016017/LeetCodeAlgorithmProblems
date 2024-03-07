from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def climbStairs(self, n: int) -> int:

        a, b = 1, 1 
        
        for i in range(n):
            a, b = b, a+b 

        return a 