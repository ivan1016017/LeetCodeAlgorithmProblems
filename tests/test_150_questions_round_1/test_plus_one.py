import unittest
from src.my_project.interviews.top_150_questions_round_1.\
plus_one import Solution

class PlusOneTestCase(unittest.TestCase):

    def test_no_nine(self):
        solution = Solution()
        output = solution.plusOne(digits=[1,2,3])
        self.assertEqual(1,output[0])
        self.assertEqual(2,output[1])
        self.assertEqual(4,output[2])
        

    def test_with_nine(self):
        solution = Solution()
        output = solution.plusOne(digits=[9,9])
        self.assertEqual(1,output[0])
        self.assertEqual(0,output[1])
        self.assertEqual(0,output[2]) 