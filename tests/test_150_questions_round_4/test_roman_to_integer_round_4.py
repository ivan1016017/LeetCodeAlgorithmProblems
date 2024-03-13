import unittest
from src.my_project.interviews.top_150_questions_round_4.\
roman_to_integer import Solution

class RomanToIntegerTestCase(unittest.TestCase):

    def test_roman_to_integer_plus_pattern(self):
        solution = Solution()
        output = solution.romanToInt(s='VII')
        self.assertEqual(7, output)

    def test_roman_to_integer_minus_pattern(self):
        solution = Solution()
        output = solution.romanToInt(s='IX')
        self.assertEqual(9, output)