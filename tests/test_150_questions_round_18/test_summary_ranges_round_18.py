import  unittest
from src.my_project.interviews.top_150_questions_round_18\
.summary_ranges import Solution

class SummaryRangesTestCase(unittest.TestCase):

    def test_empty(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[])
        target = []
        self.assertEqual(target, output)

    def test_single_element(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[1])
        target = ['1']
        self.assertEqual(target, output)

    def test_several_elements(self):
        solution = Solution()
        output = solution.summaryRanges(nums=[0,1,2,4,5,7])
        target = ["0->2","4->5","7"]
        for k, v in enumerate(target):
            self.assertEqual(v, output[k])  