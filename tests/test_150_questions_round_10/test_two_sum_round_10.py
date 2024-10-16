import unittest
from src.my_project.interviews.top_150_questions_round_10\
.two_sum import Solution

class TwoSumTestCase(unittest.TestCase):

    def test_is_two_sum(self):
        solution = Solution()
        output = solution.twoSum(nums=[2,7,11,15], target=9)
        target = [0,1]
        for k, v in enumerate(target):
            self.assertEqual(v, output[k])

    def test_is_no_two_sum(self):
        solution = Solution()
        output = solution.twoSum(nums=[2,7,11,15], target=0)
        target = -1
        self.assertEqual(output, target)