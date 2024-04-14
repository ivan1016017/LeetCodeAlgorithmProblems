import unittest
from src.my_project.interviews.top_150_questions_round_5.\
majority_element import Solution

class MajorityElementTestCase(unittest.TestCase):

    def test_is_mority_element(self):
        solution = Solution()
        target = 3 
        output = solution.majorityElement(nums=[3,2,3])
        self.assertEqual(target, output)

    def test_is_no_mority_element(self):
        solution = Solution()
        target = -1
        output = solution.majorityElement(nums=[3,2,1])
        self.assertEqual(target, output)