import unittest
from src.my_project.interviews.top_150_questions_round_8\
.best_time_to_sell_stocks import Solution


class BestTimeToSellTestCase(unittest.TestCase):

    def test_best_time_to_sell(self):
        solution = Solution()
        output = solution.maxProfit(prices=[7,1,5,3,6,4])
        target = 5
        self.assertEqual(output, target)