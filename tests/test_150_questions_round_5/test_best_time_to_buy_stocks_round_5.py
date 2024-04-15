import unittest
from src.my_project.interviews.top_150_questions_round_5.\
best_time_to_buy_stocks import Solution

class BestTimeToBuyStocksTestCase(unittest.TestCase):

    def test_best_time_to_buy(self):
        solution = Solution()
        target = 5
        output = solution.maxProfit(prices=[7,1,5,3,6,4])
        self.assertEqual(target, output)