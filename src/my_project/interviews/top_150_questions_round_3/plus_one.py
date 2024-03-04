from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        len_digits = len(digits)

        for i in range(len_digits-1,-1,-1):

            if digits[i] != 9: 
                digits[i] += 1
                break 
            else: 
                digits[i] = 0


        if digits[0] == 0:
            digits = [1] + digits

        return digits

            