import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_21_reverse_words_in_string import Solution

class ReverseWordsInStringTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.reverseWords(s = "the sky is blue")
        target = "blue is sky the"
        self.assertEqual(target, output)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.reverseWords(s = "  hello world  ")
        target = "world hello"
        self.assertEqual(target, output)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.reverseWords(s = "a good   example")
        target = "example good a"
        self.assertEqual(target, output)