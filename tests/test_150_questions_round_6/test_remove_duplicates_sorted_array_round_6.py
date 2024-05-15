import unittest
from src.my_project.interviews.top_150_questions_round_6.\
remove_duplicates_sorted_array import Solution

class RemoveDuplicatesTestCase(unittest.TestCase):

    def test_remove_duplicates(self):
        solution = Solution()
        output = solution.removeDuplicates(nums = [1,1,2])
        target = 2 
        self.assertEqual(target, output)