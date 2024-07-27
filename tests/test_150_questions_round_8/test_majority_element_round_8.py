import unittest
from src.my_project.interviews.top_150_questions_round_8.\
majority_element import Solution

class MajorityElementTestCase(unittest.TestCase):

    def test_is_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums=[3,2,3])
        target = 3
        self.assertEqual(output, target)

    def test_is_no_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums=[1,2,3,4,5])
        target = -1
        self.assertEqual(output, target)