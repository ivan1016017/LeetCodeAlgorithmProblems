import unittest
from src.my_project.interviews.top_150_questions_round_13\
.contains_duplicates_ii import Solution

class ContainsDuplicatesTestCase(unittest.TestCase):

    def test_contains_duplicates(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums=[1,2,3,1], k=3)
        self.assertTrue(output)

    def test_contains_no_duplicates(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2)
        self.assertFalse(output)