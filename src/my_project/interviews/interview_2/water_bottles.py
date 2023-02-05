from typing import List, Union, Mapping, Collection, Optional
from abc import ABC, abstractmethod

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        answer = numBottles
        drinkable_number = numBottles
        

        while drinkable_number//numExchange >=1: 
            drinkable_number, remain = drinkable_number // numExchange, drinkable_number%numExchange
            answer += drinkable_number
            drinkable_number += remain

        return answer 
