from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        answer = dict()

        for k, v in enumerate(numbers):

            if v in answer:
                return [answer[v]+1, k+1]
            else:
                answer[target - v] = k

        return []