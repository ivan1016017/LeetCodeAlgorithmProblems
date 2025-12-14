import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_32_substring_concat_all_words import Solution

class SubstringConcatAllWordsTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])
        target = [0,9] 
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"])
        target = []
        self.assertEqual(output, target)