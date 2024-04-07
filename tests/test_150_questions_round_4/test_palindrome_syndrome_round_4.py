import unittest
from src.my_project.interviews.top_150_questions_round_4.\
palindrome_number import Solution

class PalindromeNumberTestCase(unittest.TestCase):

    def test_is_palindrome(self):
        solution = Solution()
        input = 121
        output = solution.isPalindrome(x=input)
        self.assertTrue(output)

    def test_is_no_palindrome(self):
        solution = Solution()
        input = 122
        output = solution.isPalindrome(x=input)
        self.assertFalse(output)