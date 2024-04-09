import unittest
from src.my_project.interviews.top_150_questions_round_4.\
sqrtx import Solution

class SqrtxTestCase(unittest.TestCase):

    def test_perfect_sqrtx(self):
        solution = Solution()
        input = 4
        target = 2
        output = solution.mySqrt(x=input)
        self.assertEqual(target, output)

    def test_non_perfect_sqrtx(self):
        solution = Solution()
        input = 8
        target = 2
        output = solution.mySqrt(x=input)
        self.assertEqual(target, output)