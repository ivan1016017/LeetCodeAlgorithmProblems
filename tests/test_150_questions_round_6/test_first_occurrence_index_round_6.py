import unittest 
from src.my_project.interviews.top_150_questions_round_6.\
first_occurrence_index import Solution

class FindFirstOccurrenceIndexTestCase(unittest.TestCase):

    def test_found_index(self):
        solution = Solution()
        output = solution.strStr(haystack="sadbutsad", needle="sad")
        target = 0
        self.assertEqual(output, target)

    def test_no_found_index(self):
        solution = Solution()
        output = solution.strStr(haystack="leetcode", needle="leeto")
        target = -1
        self.assertEqual(output, target)