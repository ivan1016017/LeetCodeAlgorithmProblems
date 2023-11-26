import unittest
from src.my_project.interviews.top_150_questions_round_1.\
majority_element import Solution

class MajorityElementTestCase(unittest.TestCase):

    def test_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums = [2,2,1,1,1,2,2])
        self.assertEqual(output,2)