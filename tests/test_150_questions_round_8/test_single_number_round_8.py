import unittest
from src.my_project.interviews.top_150_questions_round_8\
.single_number import Solution

class SingleNumberTestCase(unittest.TestCase):

    def test_single_number(self):
        solution = Solution()
        output = solution.singleNumber(nums=[2,2,1])
        target = 1 
        self.assertEqual(output, target)