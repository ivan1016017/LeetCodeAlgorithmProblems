import unittest
from src.my_project.interviews.top_150_questions.\
single_number_updated_updated_updated_updated import Solution

class SingleNumberTestCase(unittest.TestCase):

    def test_single_number(self):
        solution = Solution()
        output = solution.singleNumber(nums=[1,1,2,2,7])
        self.assertEqual(output,7)