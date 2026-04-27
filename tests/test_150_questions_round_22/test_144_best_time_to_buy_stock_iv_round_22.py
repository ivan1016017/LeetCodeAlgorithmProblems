import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_144_best_time_to_buy_stock_iv import Solution


class BestTimeToBuyStockIVTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(2, self.solution.maxProfit(2, [2, 4, 1]))

    def test_example_2(self):
        self.assertEqual(7, self.solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))

    def test_single_price(self):
        self.assertEqual(0, self.solution.maxProfit(1, [5]))

    def test_no_profit(self):
        self.assertEqual(0, self.solution.maxProfit(2, [5, 4, 3, 2, 1]))

    def test_k_exceeds_half_n(self):
        self.assertEqual(7, self.solution.maxProfit(10, [1, 3, 2, 5, 4, 6]))


if __name__ == '__main__':
    unittest.main()