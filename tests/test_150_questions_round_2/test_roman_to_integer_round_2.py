import unittest
from src.my_project.interviews.top_150_questions_round_2.\
roman_to_integer import Solution

class RomanToIntegerTestCase(unittest.TestCase):
    
    def test_roman_to_integer_increasing_pattern(self):
        solution = Solution()
        output = solution.romanToInt(s='XVII')
        self.assertEqual(17, output)
        
    def test_roman_to_integer_decreasing_pattern(self):
        solution = Solution()
        output = solution.romanToInt(s='IV')
        self.assertEqual(4, output)