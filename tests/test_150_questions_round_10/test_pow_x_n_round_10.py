import unittest
from src.my_project.interviews.top_150_questions_round_10\
.pow_x_n import Solution

class PowxnTestCase(unittest.TestCase):

    def test_powxn_zero_power(self):
        solution = Solution()
        output = solution.myPow(x=2, n=0) 
        target = 1
        self.assertEqual(output, target)

    def test_powxn_negative_power(self):
        solution = Solution()
        output = solution.myPow(x=2, n=-1) 
        target = 0.5
        self.assertEqual(output, target)

    def test_powxn_odd_power(self):
        solution = Solution()
        output = solution.myPow(x=2, n=1) 
        target = 2
        self.assertEqual(output, target) 

    def test_powxn_even_power(self):
        solution = Solution()
        output = solution.myPow(x=2, n=2) 
        target = 4
        self.assertEqual(output, target) 
