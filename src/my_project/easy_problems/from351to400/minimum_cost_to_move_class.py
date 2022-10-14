from typing import List, Union
from abc import ABC, abstractmethod

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        odd_event = 0
        even_event = 0

        for i in range(len(position)):

            if position[i] % 2 == 0:
                even_event += 1 
            else: 
                odd_event += 1 

        return min(even_event, odd_event)