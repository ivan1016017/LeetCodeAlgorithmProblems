import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_54_basic_calculator import Solution

class BasicCalculatorTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.calculate(s = "1 + 1")
        target = 2
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.calculate(s = " 2-1 + 2 ")
        target =  3
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.calculate(s = "(1+(4+5+2)-3)+(6+8)")
        target =  23
        self.assertEqual(output, target)        