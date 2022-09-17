from typing import List, Union
from abc import ABC, abstractmethod
from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        solution = 0
        solution_dict = defaultdict(int)

        for num in nums:
            solution_dict[num] += 1 

        for key, value in solution_dict.items():
            
            if value == 1:
                solution += key 
        
        return solution 




