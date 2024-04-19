import unittest
from src.my_project.interviews.top_150_questions_round_5.\
find_index_first_occurrence import Solution

class FindIndexFirstOccurrenceTestCase(unittest.TestCase):

    def test_find_index(self):
        solution = Solution()
        target = 0
        output = solution.strStr(haystack="sadbutsad", needle="sad")
        self.assertEqual(target, output)

    def test_no_find_index(self):
        solution = Solution()
        target = -1
        output = solution.strStr(haystack="leetcode", needle="leeto")
        self.assertEqual(target, output)


