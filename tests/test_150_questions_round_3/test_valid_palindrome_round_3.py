import unittest
from src.my_project.interviews.top_150_questions_round_3.\
valid_palindrome import Solution

class ValidPalindromeTestCase(unittest.TestCase):

    def test_is_valid_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(s='aba')
        self.assertTrue(output)

    def test_is_no_valid_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(s='ab')
        self.assertFalse(output)