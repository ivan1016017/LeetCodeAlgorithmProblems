import unittest
from src.my_project.interviews.top_150_questions_round_3.\
pow_x_n import Solution

class PowxnTestCase(unittest.TestCase):

    def test_zero_base(self):
        solution = Solution()
        output = solution.myPow(x=2, n=0)
        self.assertEqual(1, output)

    def test_negative_base(self):
        solution = Solution()
        output = solution.myPow(x=2, n=-1)
        self.assertEqual(1/2, output)

    def test_even_base(self):
        solution = Solution()
        output = solution.myPow(x=2, n=2)
        self.assertEqual(4, output)

    def test_odd_base(self):
        solution = Solution()
        output = solution.myPow(x=2, n=1)
        self.assertEqual(2, output)

