import unittest
from src.my_project.interviews.top_150_questions_round_2.\
plus_one import Solution

class PlusOneTestCase(unittest.TestCase):

    def test_plus_one_length_one(self):
        solution = Solution()
        output = solution.plusOne([1])
        self.assertEqual(2, output[0])

    def test_plus_one_length_two(self):
            solution = Solution()
            output = solution.plusOne([9])
            self.assertEqual(1, output[0])
            self.assertEqual(0, output[1])