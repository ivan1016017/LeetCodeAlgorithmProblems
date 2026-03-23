import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_110_2d_matrix import Solution


class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))

    def test_target_not_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 13))

    def test_target_first_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))

    def test_target_last_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 60))

    def test_single_element_found(self):
        self.assertTrue(self.solution.searchMatrix([[5]], 5))

    def test_single_element_not_found(self):
        self.assertFalse(self.solution.searchMatrix([[5]], 3))


if __name__ == '__main__':
    unittest.main()