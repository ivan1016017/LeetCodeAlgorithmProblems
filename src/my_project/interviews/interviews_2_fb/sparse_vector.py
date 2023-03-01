from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import numpy as np 

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums 
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        temp = 0

        for i in range(len(self.nums)):
            temp += self.nums[i]*vec.nums[i]
        return temp
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

print(np.dot([1,2],[3,4]))