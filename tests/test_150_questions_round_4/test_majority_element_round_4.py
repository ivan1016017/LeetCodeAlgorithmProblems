import unittest
from src.my_project.interviews.top_150_questions_round_4.\
majority_element import Solution

class MajorityElementTestCase(unittest.TestCase):

    def test_is_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums=[3,2,3])
        self.assertEqual(3, output)

    def test_is_no_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums=[1,2,3])
        self.assertEqual(-1, output)
