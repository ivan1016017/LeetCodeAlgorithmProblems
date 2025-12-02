import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_06_rotate_array import Solution

class RotateArrayTestCase(unittest.TestCase):

    def test_rotate_array_i(self):
        solution = Solution()
        output = solution.rotate(nums = [1,2,3,4,5,6,7], k = 3)
        target = [5,6,7,1,2,3,4]
        self.assertEqual(output, target)        