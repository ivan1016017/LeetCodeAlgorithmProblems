import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_135_coin_change import Solution


class CoinChangeTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_example_3(self):
        self.assertEqual(self.solution.coinChange([1], 0), 0)

    def test_single_coin_exact(self):
        self.assertEqual(self.solution.coinChange([5], 5), 1)

    def test_large_amount(self):
        self.assertEqual(self.solution.coinChange([1, 5, 10, 25], 100), 4)

    def test_no_solution_zero_amount(self):
        self.assertEqual(self.solution.coinChange([3, 7], 0), 0)

    def test_single_coin_multiple(self):
        self.assertEqual(self.solution.coinChange([3], 9), 3)
