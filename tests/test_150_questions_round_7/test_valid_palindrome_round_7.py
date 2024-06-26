import unittest
from src.my_project.interviews.top_150_questions_round_7.\
valid_palindrome import Solution

class ValidPalindromeTestCase(unittest.TestCase):

    def test_valid_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(s="A man, a plan, a canal: Panama")
        self.assertTrue(output)

    def test_no_valid_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(s="race a car")
        self.assertFalse(output)