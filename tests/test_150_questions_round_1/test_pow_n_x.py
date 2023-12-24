import unittest
from src.my_project.interviews.top_150_questions_round_1.\
pow_n_x  import Solution

class PownxTestCase(unittest.TestCase):

    def test_none(self):
        solution = Solution()
        output = solution.myPow(x=4, n=0)
        self.assertEqual(1,output) 

    def test_negative(self):
        solution = Solution()
        output = solution.myPow(x=2, n=-1)
        self.assertEqual(0.5,output) 

    def test_odd_power(self):
        solution = Solution()
        output = solution.myPow(x=3, n=3)
        self.assertEqual(27,output) 

    def test_even_power(self):
        solution = Solution()
        output = solution.myPow(x=2, n=2)
        self.assertEqual(4,output) 