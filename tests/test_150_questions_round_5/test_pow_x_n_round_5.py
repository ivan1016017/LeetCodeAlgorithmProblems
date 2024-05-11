import unittest
from src.my_project.interviews.top_150_questions_round_5.\
pow_x_n import Solution

class MyPowxnTestCase(unittest.TestCase):

    def test_power_zero(self):
        solution = Solution()
        output = solution.myPow(x=2, n=0)
        target = 1
        self.assertEqual(target, output)

    def test_power_negative(self):
        solution = Solution()
        output = solution.myPow(x=2, n=-1)
        target = 1/2
        self.assertEqual(target, output)

    def test_power_odd(self):
        solution = Solution()
        output = solution.myPow(x=2, n=1)
        target = 2
        self.assertEqual(target, output)

    def test_power_even(self):
        solution = Solution()
        output = solution.myPow(x=2, n=2)
        target = 4
        self.assertEqual(target, output)
