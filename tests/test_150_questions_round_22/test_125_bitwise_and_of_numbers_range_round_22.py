import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_125_bitwise_and_of_numbers_range import Solution

class BitwiseAndOfNumbersRangeTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(5, 7), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 0), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(1, 2147483647), 0)