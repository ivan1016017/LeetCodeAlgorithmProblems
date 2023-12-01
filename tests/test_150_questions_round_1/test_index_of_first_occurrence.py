import unittest
from src.my_project.interviews.top_150_questions_round_1.\
index_of_first_occurrence import Solution

class IndexFirstOccurenceTestCase(unittest.TestCase):

    def test_needle_in_haystack(self):
        solution = Solution()
        output = solution.strStr(haystack = "sadbutsad", needle = "sad")
        self.assertEqual(output,0)

    def test_neddle_not_in_haystack(self):
        solution = Solution()
        output = solution.strStr(haystack = "leetcode", needle = "leeto")
        self.assertEqual(output,-1)