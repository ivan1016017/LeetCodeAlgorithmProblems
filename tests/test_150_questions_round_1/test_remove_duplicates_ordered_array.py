import unittest
from src.my_project.interviews.top_150_questions_round_1.\
remove_duplicates_ordered_array import Solution

class RemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        solution =  Solution()
        output = solution.removeDuplicates(nums=[1,1,2])
        self.assertEqual(output,2)