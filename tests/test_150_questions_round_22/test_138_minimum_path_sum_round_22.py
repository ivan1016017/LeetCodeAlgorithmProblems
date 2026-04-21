import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_138_minimum_path_sum import Solution


class MinimumPathSumTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(7, self.solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

    def test_example_2(self):
        self.assertEqual(12, self.solution.minPathSum([[1,2,3],[4,5,6]]))

    def test_single_cell(self):
        self.assertEqual(5, self.solution.minPathSum([[5]]))

    def test_single_row(self):
        self.assertEqual(6, self.solution.minPathSum([[1,2,3]]))

    def test_single_column(self):
        self.assertEqual(6, self.solution.minPathSum([[1],[2],[3]]))


if __name__ == '__main__':
    unittest.main()