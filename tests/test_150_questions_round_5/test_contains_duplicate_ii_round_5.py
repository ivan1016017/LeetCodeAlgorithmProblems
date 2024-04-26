import unittest
from src.my_project.interviews.top_150_questions_round_5.\
contains_duplicate_ii import Solution

class ContainsDuplicateTestCase(unittest.TestCase):

    def test_contains_duplicate(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums=[1,2,3,1], k=3)
        self.assertTrue(output)

    def test_contains_no_duplicate(self):
        solution = Solution()
        output = solution.containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2)
        self.assertFalse(output)

def sample():

    print('testing feature')