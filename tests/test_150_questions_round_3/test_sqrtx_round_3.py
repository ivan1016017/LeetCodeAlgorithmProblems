import unittest
from src.my_project.interviews.top_150_questions_round_3.\
sqrtx import Solution

class SqrtxTestCase(unittest.TestCase):

    def test_perfect_sqrt(self):
        solution = Solution()
        output = solution.mySqrt(x=4)
        self.assertEqual(2,output)

    def test_no_perfect_sqrt(self):
        solution = Solution()
        output = solution.mySqrt(x=5)
        self.assertEqual(2,output)