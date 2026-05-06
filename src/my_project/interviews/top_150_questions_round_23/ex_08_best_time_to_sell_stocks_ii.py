from typing import List, Union, Collection, Mapping, Optional
from abc import ABC

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        peak = None
        valley = None
        len_prices = len(prices)
        result = 0 

        while i < len(prices) - 1:

            while i < len_prices - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]

            while i < len_prices - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]

            result += peak - valley
        
        return result
