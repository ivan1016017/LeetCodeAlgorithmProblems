import unittest
from src.my_project.interviews.top_150_questions_round_4.\
plus_one import Solution

class PlusOneTestCase(unittest.TestCase):

    def test_plus_one_pattern_one(self):
        solution = Solution()
        input = [9,9]
        target = [1,0,0]
        output = solution.plusOne(digits=input)
        for k,v in enumerate(target):
            self.assertEqual(v,output[k])

    def test_plus_one_pattern_two(self):
        solution = Solution()
        input = [1,9]
        target = [2,0]
        output = solution.plusOne(digits=input)
        for k,v in enumerate(target):
            self.assertEqual(v,output[k])