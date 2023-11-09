import unittest
from src.my_project.interviews.top_150_questions.\
valid_parentheses_updated_updated_updated_updated import Solution

class ValidParenthesesTestCase(unittest.TestCase):

    def test_incomplete_parentheses(self):
        solution = Solution()
        output = solution.isValid(s=')')
        self.assertFalse(output)

    def test_complete_parentheses(self):
        solution = Solution()
        output = solution.isValid(s='()()(())')
        self.assertTrue(output)

    def test_wrong_parentheses(self):
        solution = Solution()
        output = solution.isValid(s='[)')
        self.assertFalse(output)