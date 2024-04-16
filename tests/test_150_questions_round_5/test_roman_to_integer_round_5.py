import unittest
from src.my_project.interviews.top_150_questions_round_5.\
roman_to_integer import Solution

class RomanToIntegerTestCase(unittest.TestCase):

    def test_roman_to_integer_pattern_one(self):
        solution = Solution()
        target = 7
        output = solution.romanToInt(s='VII')
        self.assertEqual(target, output)

    def test_roman_to_integer_pattern_two(self):
        solution = Solution()
        target = 9
        output = solution.romanToInt(s='IX')
        self.assertEqual(target, output)