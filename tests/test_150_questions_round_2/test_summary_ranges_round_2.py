import unittest
from src.my_project.interviews.top_150_questions_round_2.\
summary_ranges import Solution

class SummaryRangesTestCase(unittest.TestCase):

    def test_summary_ranges_empty(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[])
        self.assertEqual([],output)

    def test_summary_ranges_single_element(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[0])
        self.assertEqual('0',output[0])

    def test_summary_ranges_multiply_elements(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[0,1,2,4,5,7])
        self.assertEqual("0->2", output[0])
        self.assertEqual("4->5", output[1])
        self.assertEqual("7", output[2])

    