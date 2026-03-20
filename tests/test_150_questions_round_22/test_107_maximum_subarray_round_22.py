import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_107_maximum_subarray import Solution


class MaximumSubarrayTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maxSubArray([5, 4, -1, 7, 8]), 23)