import unittest
from src.my_project.interviews.top_150_questions_round_10\
.valid_palindrome import Solution

class ValidPalindromeTestCase(unittest.TestCase):

    def test_is_valid_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(s="A man, a plan, a canal: Panama")
        self.assertTrue(output)

    def test_is_no_valid_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(s="race a car")
        self.assertFalse(output)
