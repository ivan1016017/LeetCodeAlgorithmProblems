import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_108_maximum_circular_subarray import Solution


class MaximumCircularSubarrayTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(3, self.solution.maxSubarraySumCircular([1, -2, 3, -2]))

    def test_example_2(self):
        self.assertEqual(10, self.solution.maxSubarraySumCircular([5, -3, 5]))

    def test_example_3(self):
        self.assertEqual(-2, self.solution.maxSubarraySumCircular([-3, -2, -3]))