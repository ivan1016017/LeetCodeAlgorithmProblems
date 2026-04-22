import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_139_unique_paths_ii import Solution


class UniquePathsIITestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(2, self.solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

    def test_example_2(self):
        self.assertEqual(1, self.solution.uniquePathsWithObstacles([[0,1],[0,0]]))

    def test_obstacle_at_start(self):
        self.assertEqual(0, self.solution.uniquePathsWithObstacles([[1,0],[0,0]]))

    def test_obstacle_at_end(self):
        self.assertEqual(0, self.solution.uniquePathsWithObstacles([[0,0],[0,1]]))

    def test_single_cell_no_obstacle(self):
        self.assertEqual(1, self.solution.uniquePathsWithObstacles([[0]]))

    def test_single_cell_obstacle(self):
        self.assertEqual(0, self.solution.uniquePathsWithObstacles([[1]]))


if __name__ == '__main__':
    unittest.main()