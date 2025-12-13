import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_30_minimum_size_subarray_sum import Solution

class MinimumSizeSubarraySumTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
        target = 2 
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.minSubArrayLen(target = 4, nums = [1,4,4])
        target = 1
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])
        target = 0
        self.assertEqual(output, target)
