import unittest
from src.my_project.interviews.top_150_questions_round_1.\
valid_palindrome import Solution

class ValidPalindromTestCase(unittest.TestCase):

    def test_non_palindrom(self):
        solution = Solution()
        output = solution.isPalindrome(s = "race a car")
        self.assertFalse(output)


    def test_palindrome(self):
        solution = Solution()
        output = solution.isPalindrome(s = "A man, a plan, a canal: Panama")
        self.assertTrue(output)