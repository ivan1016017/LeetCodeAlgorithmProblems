import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_36_set_matrix_zeroes import Solution

class MatrixZeroesTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])
        target = [[1,0,1],[0,0,0],[1,0,1]]
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
        target = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        self.assertEqual(output, target)

