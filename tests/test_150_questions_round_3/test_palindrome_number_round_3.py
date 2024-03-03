import unittest
from src.my_project.interviews.top_150_questions_round_3.\
palindrome_number import Solution

class PalindromNumberTestCase(unittest.TestCase):

    def test_is_palindrome_number(self):
        solution = Solution()
        output = solution.isPalindrome(x=121)
        self.assertTrue(output)

    def test_is_no_palindrome_number(self):
        solution = Solution()
        output = solution.isPalindrome(x=12)
        self.assertFalse(output)
