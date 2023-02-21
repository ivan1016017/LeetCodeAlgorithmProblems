from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_value_price = math.inf 
        max_profit = 0 

        for i in range(len(prices)):
            if prices[i] < min_value_price:
                min_value_price = prices[i]
            elif prices[i] - min_value_price > max_profit:
                max_profit = prices[i] - min_value_price


        return max_profit