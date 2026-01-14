import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_48_insert_interval import Solution

class InsertIntervalsTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
        target = [[1,5],[6,9]]
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
        target = [[1,2],[3,10],[12,16]]
        self.assertEqual(output, target)

