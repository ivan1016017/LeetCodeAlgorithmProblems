import unittest
from src.my_project.interviews.top_150_questions_round_3.\
find_index_first_occurrence import Solution

class FindFirstIndexOccurrenceTestCase(unittest.TestCase):

    def test_find_first_occurrence_index(self):
        solution = Solution()
        output = solution.strStr(haystack="sadbutsad", needle="sad")
        self.assertEqual(0, output)

    def test_no_find_first_occurrence_index(self):
            solution = Solution()
            output = solution.strStr(haystack="c", needle="b")
            self.assertEqual(-1, output)