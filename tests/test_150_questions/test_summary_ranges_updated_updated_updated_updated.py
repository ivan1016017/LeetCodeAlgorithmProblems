import unittest
from src.my_project.interviews.top_150_questions.\
summary_ranges_updated_updated_updated_updated import Solution

class SummaryRangesTestCase(unittest.TestCase):

    def test_empty_range(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[])
        self.assertEqual(output,[])

    def test_single_range(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[0])
        self.assertEqual(output,['0'])

    def test_multiple_ranges(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[0,1,2,4,5,7])
        self.assertEqual(output,["0->2","4->5","7"])