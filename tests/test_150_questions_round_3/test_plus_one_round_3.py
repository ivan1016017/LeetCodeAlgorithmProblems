import unittest
from src.my_project.interviews.top_150_questions_round_3.\
plus_one import Solution

class PlusOneTestCase(unittest.TestCase):

    def test_plus_one_leading_one(self):
        solution = Solution()
        output = solution.plusOne(digits=[9])
        self.assertEqual(1,output[0])
        self.assertEqual(0,output[-1])

    def test_plus_one_no_leading_one(self):
        solution = Solution()
        output = solution.plusOne(digits=[6])
        self.assertEqual(7,output[0])
        