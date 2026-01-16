import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_50_valid_parentheses import Solution

class ValidParenthesesTestCase(unittest.TestCase):

    def test_is_valid_parentheses(self):
        solution = Solution()
        output = solution.isValid(s='()')
        self.assertTrue(output)

    def test_is_no_valid_parentheses_pattern_1(self):
        solution = Solution()
        output = solution.isValid(s='(]')
        self.assertFalse(output)

    def test_is_no_valid_parentheses_pattern_2(self):
        solution = Solution()
        output = solution.isValid(s='((')
        self.assertFalse(output)