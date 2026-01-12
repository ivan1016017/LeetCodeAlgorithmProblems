import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_45_longest_consecutive_sequence import Solution

class LongestConsecutiveSequenceTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.longestConsecutive(nums = [100,4,200,1,3,2])
        target = 4
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])
        target = 9
        self.assertEqual(output, target)

    def test_third_pattern(self):
        solution = Solution()
        output = solution.longestConsecutive(nums = [1,0,1,2])
        target = 3
        self.assertEqual(output, target)        