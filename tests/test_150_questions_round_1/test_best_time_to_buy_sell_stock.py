import unittest
from src.my_project.interviews.top_150_questions_round_1.\
best_time_to_buy_sell_stock import Solution

class BestTimeToSellBuyTestCase(unittest.TestCase):

    def test_max_profit(self):
        solution = Solution()
        output = solution.maxProfit(prices = [7,1,5,3,6,4])
        self.assertEqual(output,5)