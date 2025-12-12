import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_27_two_sum_ii import Solution

class TwoSumIIestCase(unittest.TestCase):

    def test_is_two_sum(self):
        solution = Solution()
        output = solution.twoSum(numbers = [2,7,11,15], target = 9)
        target = [1,2]
        for k, v in enumerate(target):
            self.assertEqual(v, output[k])

    def test_is_no_two_sum(self):
        solution = Solution()
        output = solution.twoSum(numbers=[2,7,11,15], target=0)
        target = []
        self.assertEqual(output, target)