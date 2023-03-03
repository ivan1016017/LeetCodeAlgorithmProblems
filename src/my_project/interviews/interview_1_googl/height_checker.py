from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        original = heights.copy()
        heights.sort()
        answer = 0
        len_heights = len(heights)

        for i in range(len_heights):
            if original[i] != heights[i]:
                answer += 1 

        return answer 