import unittest
from src.my_project.interviews.top_150_questions_round_1.\
palindrome_number import Solution

class PalindromeNumberTestCase(unittest.TestCase):

    def test_palindrome_number(self):
        solution = Solution()
        output = solution.isPalindrome(x = 121)
        self.assertTrue(output)