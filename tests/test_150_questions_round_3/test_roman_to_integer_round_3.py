import unittest
from src.my_project.interviews.top_150_questions_round_3.\
roman_to_integer import Solution

class RomanToIntegerTestCase(unittest.TestCase):

    def test_roman_to_integer_increasing(self):
        solution = Solution()
        output = solution.romanToInt(s="XXI")
        self.assertEqual(21, output)

    def test_roman_to_integer_decreasing(self):
            solution = Solution()
            output = solution.romanToInt(s="IX")
            self.assertEqual(9, output)
