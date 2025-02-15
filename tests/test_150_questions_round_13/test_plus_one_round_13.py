import unittest
from src.my_project.interviews.top_150_questions_round_13\
.plus_one import Solution


class PlusOneTestCase(unittest.TestCase):

    def test_leading_one(self):
        solution = Solution()
        output = solution.plusOne(digits=[9])
        target = [1, 0] 
        for k, v in enumerate(target):
            self.assertEqual(v, output[k])

    def test_no_leading_one(self):
        solution = Solution()
        output = solution.plusOne(digits=[1, 2])
        target = [1, 3] 
        for k, v in enumerate(target):
            self.assertEqual(v, output[k])