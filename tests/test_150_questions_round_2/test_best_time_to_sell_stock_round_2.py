import unittest
import math
from src.my_project.interviews.top_150_questions_round_2.\
best_time_to_sell_stock import Solution

class BestTimeToSellTestCase(unittest.TestCase):
    
    def test_best_time_to_sell(self):
        solution = Solution()
        output = solution.maxProfit(prices = [7,1,5,3,6,4])
        self.assertEqual(5, output)