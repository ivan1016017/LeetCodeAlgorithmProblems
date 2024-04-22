import unittest
from src.my_project.interviews.top_150_questions_round_5.\
word_pattern import Solution

class WordPatternTestCase(unittest.TestCase):

    def test_is_word_pattern(self):
        solution = Solution()
        output = solution.wordPattern(pattern="abba", s="dog cat cat dog")
        self.assertTrue(output)

    def test_is_no_word_pattern_case_one(self):
        solution = Solution()
        output = solution.wordPattern(pattern="aab", s="bcb")
        self.assertFalse(output)

    def test_is_no_word_pattern_case_two(self):
        solution = Solution()
        output = solution.wordPattern(pattern='aa', s='bc')
        self.assertFalse(output)


def sample():
    print('testing')