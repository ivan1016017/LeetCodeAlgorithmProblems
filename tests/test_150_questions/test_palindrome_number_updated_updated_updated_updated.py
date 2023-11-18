import unittest
from src.my_project.interviews.top_150_questions.\
palindrome_number_updated_updated_updated_updated import Solution

class PalindromNumberTestCas(unittest.TestCase):

    def test_is_palindrome_number(self):
        solution = Solution()
        output = solution.isPalindrome('121')
        self.assertTrue(output)

    def test_is_no_palindrome_number(self):
        solution = Solution()
        output = solution.isPalindrome('123')
        self.assertFalse(output)