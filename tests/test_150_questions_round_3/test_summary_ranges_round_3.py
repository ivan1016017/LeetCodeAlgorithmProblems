import unittest
from src.my_project.interviews.top_150_questions_round_3.\
summary_ranges import Solution

class SummaryRangesTestCase(unittest.TestCase):

    def test_empty(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[])
        self.assertEqual([], output)

    def test_one_range(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[1])
        self.assertEqual("1", output[0])

    def test_several_ranges(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[0,1,2,4,5,7])
        test_range = ["0->2","4->5","7"]

        for k, v in enumerate(test_range):
            self.assertEqual(v, output[k])

    