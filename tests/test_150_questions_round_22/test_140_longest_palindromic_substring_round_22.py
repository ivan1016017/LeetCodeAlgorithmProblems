import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_140_longest_palindromic_substring import Solution


class LongestPalindromicSubstringTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.longestPalindrome("babad")
        self.assertIn(result, ("bab", "aba"))

    def test_example_2(self):
        self.assertEqual("bb", self.solution.longestPalindrome("cbbd"))

    def test_single_char(self):
        self.assertEqual("a", self.solution.longestPalindrome("a"))

    def test_all_same(self):
        self.assertEqual("aaaa", self.solution.longestPalindrome("aaaa"))

    def test_no_palindrome_longer_than_one(self):
        result = self.solution.longestPalindrome("abcd")
        self.assertEqual(1, len(result))

    def test_even_palindrome(self):
        self.assertEqual("abba", self.solution.longestPalindrome("cabba"))

    def test_full_string_palindrome(self):
        self.assertEqual("racecar", self.solution.longestPalindrome("racecar"))


if __name__ == '__main__':
    unittest.main()
