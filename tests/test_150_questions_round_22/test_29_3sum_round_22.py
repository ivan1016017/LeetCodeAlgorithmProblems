import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_29_3sum import Solution

class ThreeSumTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.threeSum(nums = [-1,0,1,2,-1,-4])
        target = [(-1,-1,2),(-1,0,1)]
        output.sort()
        target.sort()
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.threeSum(nums = [0,1,1])
        target = []
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.threeSum(nums = [0,0,0])
        target = [(0,0,0)]
        self.assertEqual(output, target)        