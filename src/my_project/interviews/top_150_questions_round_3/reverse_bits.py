from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def reverseBits(self, n: int) -> int:
        
        return int((('{0:032b}'.format(n))[::-1]),2)