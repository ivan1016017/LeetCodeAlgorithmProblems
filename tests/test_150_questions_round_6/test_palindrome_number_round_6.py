import unittest
from src.my_project.interviews.top_150_questions_round_6.\
palindrome_number import Solution

class PalindromeNumberTestCase(unittest.TestCase):

    def test_is_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(121)
        self.assertTrue(output)

    def test_is_no_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(122)
        self.assertFalse(output)