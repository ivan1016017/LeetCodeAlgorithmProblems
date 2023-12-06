import unittest
from src.my_project.interviews.top_150_questions_round_1.\
word_patterns import Solution

class WordPatternTestCase(unittest.TestCase):

    def test_word_pattern(self):
        solution = Solution()
        output = solution.wordPattern(pattern = "abba", s = "dog cat cat dog")
        self.assertTrue(output)
        

    def test_no_word_pattern(self):
        solution = Solution()
        output = solution.wordPattern(pattern = "abba", s = "dog cat cat fish")
        self.assertFalse(output)