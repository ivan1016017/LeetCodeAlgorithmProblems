from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = math.inf
        max_profit = 0
        len_prices = len(prices)

        for i in range(len_prices):

            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit