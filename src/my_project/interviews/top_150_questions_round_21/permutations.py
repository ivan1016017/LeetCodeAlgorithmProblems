from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        final_answer = list()

        def back(answer = list()):
            if len(answer) == len(nums):
                final_answer.append(answer)
                return 
            
            for num in nums:
                if num not in answer:
                    new_arr = answer + [num]
                    back(new_arr)

        back()

        return final_answer