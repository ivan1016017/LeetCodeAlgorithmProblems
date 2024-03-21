import unittest
from src.my_project.interviews.top_150_questions_round_4.\
word_pattern import Solution

class WordPatternTestCase(unittest.TestCase):

    def test_is_word_pattern(self):
        solution = Solution()
        output = solution.wordPattern(pattern="abba", s="dog cat cat dog")
        self.assertTrue(output)

    def test_is_no_word_pattern(self):
        solution = Solution()
        output = solution.wordPattern(pattern="aaba", s="dog cat cat dog")
        self.assertFalse(output)


    def test_is_no_len_match(self):
        solution = Solution()
        output = solution.wordPattern(pattern="abbac", s="dog cat cat fish")
        self.assertFalse(output)