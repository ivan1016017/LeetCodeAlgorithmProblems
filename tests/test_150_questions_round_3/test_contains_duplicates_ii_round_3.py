import unittest
from src.my_project.interviews.top_150_questions_round_3.\
contains_duplicates_ii import Solution

class ContainsDuplicatesII(unittest.TestCase):

    def test_have_duplicates(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums=[1,2,3,1], k=3)
        self.assertTrue(output)


    def test_have_no_duplicates(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2)
        self.assertFalse(output)