import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_31_longest_substring_without_repeating_characters import Solution

class LongestSubstringUniqueCharactersTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.lengthOfLongestSubstring(s = "abcabcbb")
        target = 3 
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.lengthOfLongestSubstring(s = "bbbbb")
        target = 1
        self.assertEqual(output, target)