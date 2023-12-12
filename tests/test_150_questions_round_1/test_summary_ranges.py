import unittest
from src.my_project.interviews.top_150_questions_round_1.\
summary_ranges import Solution

class SummaryRangesTestCase(unittest.TestCase):

    def test_empty(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[])
        self.assertEqual([],output)

    def test_one_element(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[7])
        self.assertEqual(["7"],output)

    def test_several_elements(self):
        solution = Solution()
        output = solution.summaryRanges(nums = [0,1,2,4,5,7])
        self.assertEqual(["0->2","4->5","7"],output)