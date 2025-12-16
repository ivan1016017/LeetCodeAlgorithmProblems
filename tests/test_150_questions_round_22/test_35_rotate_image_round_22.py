import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_35_rotate_image import Solution

class RotateImageTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])
        target = [[7,4,1],[8,5,2],[9,6,3]]
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
        target = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        self.assertEqual(output, target)

