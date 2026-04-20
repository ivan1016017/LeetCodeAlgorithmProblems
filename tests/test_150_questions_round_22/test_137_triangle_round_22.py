import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_137_triangle import Solution


class TriangleTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(11, self.solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))

    def test_example_2(self):
        self.assertEqual(-10, self.solution.minimumTotal([[-10]]))

    def test_single_row(self):
        self.assertEqual(5, self.solution.minimumTotal([[5]]))

    def test_two_rows(self):
        self.assertEqual(3, self.solution.minimumTotal([[1],[2,3]]))


if __name__ == '__main__':
    unittest.main()