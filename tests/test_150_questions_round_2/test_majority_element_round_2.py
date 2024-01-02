import unittest
from src.my_project.interviews.top_150_questions_round_2.\
majority_element import Solution

class MajorityElementTestCase(unittest.TestCase):
    
    def test_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums = [3,2,3])
        self.assertEqual(3, output)
        
    def test_no_majority_element(self):
        solution = Solution()
        output = solution.majorityElement(nums = [1, 2, 3, 4])
        self.assertEqual(-1, output)