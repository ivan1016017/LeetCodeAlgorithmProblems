import unittest
from src.my_project.interviews.top_150_questions_round_7.\
find_index_first_occurrence import Solution

class FindIndexFirstOccurrenceTestCase(unittest.TestCase):

    def test_find_index(self):
        solution = Solution()
        output = solution.strStr(haystack="sadbutsad", needle="sad")
        target = 0
        self.assertEqual(output, target)


    def test_find_no_index(self):
        solution = Solution()
        output = solution.strStr(haystack="leetcode", needle="leeto")
        target = -1 
        self.assertEqual(output, target)