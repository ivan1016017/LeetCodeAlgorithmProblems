import unittest
from src.my_project.interviews.top_150_questions_round_4.\
summary_ranges import Solution

class SummaryRangesTestCase(unittest.TestCase):

    def test_non_empty(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[0,1,2,4,5,7])
        target = ["0->2","4->5","7"]
        for k, v in enumerate(target):
            self.assertEqual(v, output[k])

    def test_one_element(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[7])
        target = ["7"]
        for k, v in enumerate(target):
            self.assertEqual(v, output[k])

    def test_empty(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[])
        self.assertEqual([],output)