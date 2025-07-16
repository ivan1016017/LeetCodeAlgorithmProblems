import unittest
from src.my_project.interviews.top_150_questions_round_18\
.roman_to_integer import Solution

class RomanToIntegerTestCase(unittest.TestCase):

    def test_patter_one(self):
        solution = Solution()
        output = solution.romanToInt(s='VII')
        target = 7
        self.assertEqual(output, target)

    def test_patter_two(self):
        solution = Solution()
        output = solution.romanToInt(s='IX')
        target = 9
        self.assertEqual(output, target)