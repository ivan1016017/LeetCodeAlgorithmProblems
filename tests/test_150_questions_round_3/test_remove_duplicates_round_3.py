import unittest
from src.my_project.interviews.top_150_questions_round_3.\
remove_duplicates import Solution

class RemoveDuplicatesTestCase(unittest.TestCase):

    def test_remove_duplicates(self):
        solution = Solution()
        output = solution.removeDuplicates(nums=[1,1,2])
        self.assertEqual(2, output)