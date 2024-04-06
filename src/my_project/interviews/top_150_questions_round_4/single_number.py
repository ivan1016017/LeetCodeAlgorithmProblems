from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0

        for num in nums: 
            answer ^= num 

        return answer 