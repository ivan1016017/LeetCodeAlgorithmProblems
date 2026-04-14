import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_131_max_points_in_a_line import Solution

class MaxPointsInALineTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_three_collinear_points(self):
        self.assertEqual(3, self.solution.maxPoints([[1, 1], [2, 2], [3, 3]]))

    def test_six_points(self):
        self.assertEqual(4, self.solution.maxPoints(
            [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))

    def test_single_point(self):
        self.assertEqual(1, self.solution.maxPoints([[0, 0]]))

    def test_two_points(self):
        self.assertEqual(2, self.solution.maxPoints([[0, 0], [1, 1]]))

    def test_vertical_line(self):
        self.assertEqual(3, self.solution.maxPoints([[1, 1], [1, 2], [1, 3]]))

    def test_horizontal_line(self):
        self.assertEqual(3, self.solution.maxPoints([[1, 1], [2, 1], [3, 1]]))


