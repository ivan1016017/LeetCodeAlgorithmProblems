import unittest
from src.my_project.interviews.top_150_questions_round_2.\
sqrtx import Solution

class SqrtxTestCase(unittest.TestCase):

    def test_perfect_sqrtx(self):
        solution = Solution()
        output = solution.mySqrt(x=4)
        self.assertEqual(2, output)

    def test_imperfect_sqrtx(self):
            solution = Solution()
            output = solution.mySqrt(x=8)
            self.assertEqual(2, output)