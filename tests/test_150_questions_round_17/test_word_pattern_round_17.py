import unittest
from src.my_project.interviews.top_150_questions_round_17\
.word_pattern import Solution

class WordPatternTestCase(unittest.TestCase):

    def test_is_word_pattern(self):
        solution = Solution()
        output = solution.wordPattern(pattern="abba", s="dog cat cat dog")
        self.assertTrue(output)

    def test_is_no_word_pattern_one(self):
        solution = Solution()
        output = solution.wordPattern(pattern="abc", s="dog cat cat fish")
        self.assertFalse(output)

    def test_is_no_word_pattern_two(self):
        solution = Solution()
        output = solution.wordPattern(pattern="aa", s="dog cat cat fish")
        self.assertFalse(output)