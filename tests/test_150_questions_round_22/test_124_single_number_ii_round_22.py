import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_124_single_number_ii import Solution

class SingleNumberIITestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.singleNumber([2, 2, 3, 2]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)

    def test_single_element(self):
        self.assertEqual(self.solution.singleNumber([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.singleNumber([-2, -2, 1, -2]), 1)

    def test_zero_is_single(self):
        self.assertEqual(self.solution.singleNumber([5, 5, 5, 0]), 0)