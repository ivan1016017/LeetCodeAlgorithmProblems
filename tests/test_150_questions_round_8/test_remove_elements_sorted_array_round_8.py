import unittest
from src.my_project.interviews.top_150_questions_round_8\
.remove_elements_sorted_array import Solution

class RemoveElementsSortedArray(unittest.TestCase):

    def test_sorted_array(self):
        solution = Solution()
        output = solution.removeDuplicates(nums=[1,1,2])
        target = 2
        self.assertEqual(output, target)