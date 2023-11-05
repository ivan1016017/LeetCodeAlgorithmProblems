import unittest
from src.my_project.interviews.top_150_questions.\
    two_sum_updated_updated_updated import Solution

class TwoSumTestCase(unittest.TestCase):

    def test_identify_first_two_index(self):

        solution = Solution()
        output = solution.twoSum(nums=[2,7,11,15],target=9)
        self.assertEqual(output,[0,1])
        

    def test_identify_last_two_indices(self):

        solution = Solution()
        output = solution.twoSum(nums=[3,2,4],target=6)
        self.assertEqual(output,[1,2])

    def test_no_value(self):

        solution = Solution()
        output = solution.twoSum(nums=[3,2,4],target=60)
        self.assertIsNone(output)