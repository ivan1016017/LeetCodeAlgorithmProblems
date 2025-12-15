import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_33_minimum_window_substring import Solution

class MinimumWindowSubstringTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.minWindow(s = "ADOBECODEBANC", t = "ABC")
        target = "BANC"
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.minWindow(s = "a", t = "a")
        target = "a"
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.minWindow(s = "a", t = "aa")
        target = ""
        self.assertEqual(output, target)        