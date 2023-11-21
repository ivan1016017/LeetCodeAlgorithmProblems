import unittest
from src.my_project.interviews.top_150_questions.\
pow_x_n_updated_updated_updated_updated import Solution

class PowxnTestCase(unittest.TestCase):

    def test_zero(self):
        solution = Solution()
        output = solution.myPow(x=7,n=0)
        self.assertEqual(output,1)

    def test_negative(self):
        solution = Solution()
        output = solution.myPow(x=7,n=-1)
        self.assertEqual(output,1/7)

    def test_positive(self):
        solution = Solution()
        output = solution.myPow(x=7,n=1)
        self.assertEqual(output,7)