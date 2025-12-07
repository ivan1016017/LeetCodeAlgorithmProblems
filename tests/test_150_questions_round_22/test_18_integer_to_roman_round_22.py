import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_18_integer_to_roman import Solution

class IntegerToRomanTestCase(unittest.TestCase):

    def test_patter_one(self):
        solution = Solution()
        output = solution.intToRoman(num = 3749)
        target = "MMMDCCXLIX"
        self.assertEqual(output, target)

    def test_patter_two(self):
        solution = Solution()
        output = solution.intToRoman(num = 58)
        target = "LVIII"
        self.assertEqual(output, target)