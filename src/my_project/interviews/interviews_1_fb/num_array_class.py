from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        

    def sumRange(self, left: int, right: int) -> int:

        return sum(self.nums[left:right+1])
    

