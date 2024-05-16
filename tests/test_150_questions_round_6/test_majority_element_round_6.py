import unittest
from src.my_project.interviews.top_150_questions_round_6.\
majority_element import Solution

class MajorityElementTestCase(unittest.TestCase):

    def test_there_is_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums = [3, 2, 3])
        target = 3 
        self.assertEqual(target, output)

    def test_there_is_no_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums=[1, 2, 3, 4, 5])
        target = -1
        self.assertEqual(target, output)