import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_04_remove_duplicates_ii import Solution

class RemoveDuplicatesTestCaseII(unittest.TestCase):
    def test_remove_duplicates(self):
        solution = Solution()
        output = solution.removeDuplicates(nums = [1,1,1,2,2,3])
        target = 5
        self.assertEqual(output, target)