from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def merge(self, 
              nums1: List[int], 
              m: int, nums2: List[int], 
              n: int) -> None:
        
        nums1[m: m+n] = nums2 
        nums1.sort()

        return nums1