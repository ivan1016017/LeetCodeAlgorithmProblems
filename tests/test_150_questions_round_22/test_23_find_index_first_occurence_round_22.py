import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_23_find_index_first_occurence import Solution

class FirstOccurrenceIndexTestCase(unittest.TestCase):

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