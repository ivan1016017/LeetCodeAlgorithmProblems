from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums 
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        answer = 0
        for i in range(len(self.nums)):
            answer += self.nums[i]*vec.nums[i]

        return answer 
    
class SparseVectorTwo:
    def __init__(self, nums: List[int]):
        self.nums = nums 
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVectorTwo') -> int:
        answer = 0
        for i in range(len(self.nums)):
            answer += self.nums[i]*vec.nums[i]

        return answer 
    
