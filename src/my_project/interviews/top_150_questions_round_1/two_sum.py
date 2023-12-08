from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic_answer = dict()

        for k, v in enumerate(nums):
            if v in dic_answer:
                return [dic_answer[v],k]
            dic_answer[target-v] = k