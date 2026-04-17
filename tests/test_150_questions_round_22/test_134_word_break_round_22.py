import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_134_word_break import Solution


class WordBreakTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_single_char_true(self):
        s = "a"
        wordDict = ["a"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_single_char_false(self):
        s = "b"
        wordDict = ["a"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_reuse_word(self):
        s = "aaaaaaa"
        wordDict = ["aaaa", "aaa"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_empty_string(self):
        s = ""
        wordDict = ["a"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))