import unittest
from src.my_project.interviews.top_150_questions_round_4.\
find_index_first_occurence import Solution

class FindIndexFirstOccurrence(unittest.TestCase):

    def test_find_index_first_occurrence(self):
        solution = Solution()
        output = solution.strStr(haystack="sadbutsad", needle="sad")
        self.assertEqual(0, output)

    def test_no_find_index_first_occurrence(self):
        solution = Solution()
        output = solution.strStr(haystack="leetcode", needle="leeto")
        self.assertEqual(-1, output)