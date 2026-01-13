import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_47_merge_intervals import Solution

class MergeIntervalsTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.merge(intervals = [[1,3],[2,6],[8,10],[15,18]])
        target = [[1,6],[8,10],[15,18]]
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.merge(intervals = [[1,4],[4,5]])
        target = [[1,5]]
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.merge(intervals = [[4,7],[1,4]])
        target = [[1,7]]
        self.assertEqual(output, target)        