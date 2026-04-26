import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_143_best_time_to_buy_stock_iii import Solution


class BestTimeToBuyStockIIITestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)
