import unittest
from src.my_project.interviews.top_150_questions_round_6.\
two_sum import Solution

class TwoSumTestCase(unittest.TestCase):

    def test_two_sum(self):
        solution = Solution()
        output = solution.twoSum(nums=[2,7,11,15], target=9)
        target = [0, 1]

        for k, v in enumerate(target):
            self.assertEqual(v, output[k])