import unittest
from src.my_project.interviews.top_150_questions_round_1.\
valid_parentheses import Solution

class ValidParenthesesTestCase(unittest.TestCase):

    def test_valid_parentheses(self):
        solution = Solution()
        output = solution.isValid(s = "()")
        self.assertTrue(output)

    def test_no_valid_parentheses(self):
        solution = Solution()
        output = solution.isValid(s = "())")
        self.assertFalse(output)