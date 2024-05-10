import unittest
from src.my_project.interviews.top_150_questions_round_5.\
sqrtx import Solution

class SqrtxTestCase(unittest.TestCase):

    def test_perfect_sqrtx(self):
        solution = Solution()
        output = solution.mySqrt(x=4)
        target = 2
        self.assertEqual(target, output)

    def test_imperfect_sqrtx(self):
        solution = Solution()
        output = solution.mySqrt(x=8)
        target = 2
        self.assertEqual(target, output)