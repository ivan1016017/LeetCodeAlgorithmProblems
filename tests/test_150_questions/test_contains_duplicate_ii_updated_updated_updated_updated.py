import unittest
from src.my_project.interviews.top_150_questions.\
contains_duplicate_ii_updated_updated_updated_updated import Solution

class ContainstDuplicateiiTestCase(unittest.TestCase):

    def test_duplicate_true(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)
        self.assertTrue(output)

    def test_duplicate_false(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
        self.assertFalse(output)