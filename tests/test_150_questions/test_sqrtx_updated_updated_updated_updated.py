import unittest
from src.my_project.interviews.top_150_questions.\
sqrtx_updated_updated_updated_updated import Solution

class SqrtxTestCase(unittest.TestCase):

    def test_perfect_sqrtx(self):
        solution = Solution()
        output = solution.mySqrt(x = 9)
        self.assertEqual(output,3) 

    def test_no_perfect_sqrtx(self):
        solution = Solution()
        output = solution.mySqrt(x=8) 
        self.assertEqual(output,2)