from typing import List, Union, Collection, Mapping 
from abc import ABC, abstractmethod

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        dict_solution = {}
        temp_solution = 0

        for num in candyType:
            if num not in dict_solution:
                dict_solution[num] = 1
                temp_solution += 1
            else: 
                dict_solution[num] += 1


        return min(len(candyType)//2, temp_solution)