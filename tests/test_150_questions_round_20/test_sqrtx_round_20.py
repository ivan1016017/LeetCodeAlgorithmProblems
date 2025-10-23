import unittest
from src.my_project.interviews.top_150_questions_round_20\
.sqrtx import Solution

class SqrtxTestCase(unittest.TestCase):

    def test_even_sqrtx(self):
        solution = Solution()
        output = solution.mySqrt(x=4)
        target = 2 
        self.assertEqual(output, target)

    def test_odd_sqrtx(self):
        solution = Solution()
        output = solution.mySqrt(x=8)
        target = 2 
        self.assertEqual(output, target)