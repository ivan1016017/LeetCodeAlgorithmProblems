from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        answer = list()

        mid_lenght = len(nums)//2

        for i in range(mid_lenght):
            answer.append(nums[i])
            answer.append(nums[mid_lenght+i])

        return answer