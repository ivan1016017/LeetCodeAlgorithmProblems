import unittest
from src.my_project.interviews.top_150_questions_round_1.\
roman_to_integer import Solution

class RomanToIntegerTestCase(unittest.TestCase):

    def test_roman_to_integer_increasing(self):
        solution = Solution()
        output = solution.romanToInt(s='XXVII')
        self.assertEqual(output,27)
        
    def test_roman_to_integer_decreasing(self):
        solution = Solution()
        output = solution.romanToInt(s='XIX')
        self.assertEqual(output,19)