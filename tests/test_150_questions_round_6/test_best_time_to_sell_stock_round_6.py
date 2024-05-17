import unittest
from src.my_project.interviews.top_150_questions_round_6.\
best_time_to_sell_stock import Solution

class BestTimeToSellStockTestCase(unittest.TestCase):

    def test_max_profit(self):
        solution = Solution()
        output = solution.maxProfit(prices=[7, 1, 5, 3, 6, 4])
        target = 5
        self.assertEqual(target, output)