import unittest
from src.my_project.interviews.top_150_questions_round_20\
.finding_first_occurrence_index import Solution

class FirstOccurrenceIndex(unittest.TestCase):

    def test_first_occurrence_index(self):
        solution = Solution()
        output = solution.strStr(haystack="sadbutsad", needle="sad")
        target = 0 
        self.assertEqual(output, target)

    def test_no_first_occurrence_index(self):
        solution = Solution()
        output = solution.strStr(haystack="leetcode", needle="leeto")
        target = -1
        self.assertEqual(output, target)