import unittest
from src.my_project.interviews.top_150_questions_round_2.\
pow_x_n import Solution

class PownxTestCase(unittest.TestCase):

    def test_exponent_zero(self):
        solution = Solution()
        output = solution.myPow(x=2, n=0)
        self.assertEqual(1, output)

    def test_negative_exponent(self):
            solution = Solution()
            output = solution.myPow(x=2, n=-2)
            self.assertEqual(0.25, output)

    def test_positive_exponent(self):
            solution = Solution()
            output = solution.myPow(x=2, n=2)
            self.assertEqual(4, output)