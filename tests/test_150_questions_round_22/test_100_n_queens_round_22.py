import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_100_n_queens import Solution


class NQueensTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with n = 4, should return 2 solutions"""
        result = self.solution.totalNQueens(4)
        self.assertEqual(result, 2)
    
    def test_example_2(self):
        """Test with n = 1, should return 1 solution"""
        result = self.solution.totalNQueens(1)
        self.assertEqual(result, 1)
    
    def test_n_2(self):
        """Test with n = 2, should return 0 solutions"""
        result = self.solution.totalNQueens(2)
        self.assertEqual(result, 0)
    
    def test_n_3(self):
        """Test with n = 3, should return 0 solutions"""
        result = self.solution.totalNQueens(3)
        self.assertEqual(result, 0)
    
    def test_n_5(self):
        """Test with n = 5, should return 10 solutions"""
        result = self.solution.totalNQueens(5)
        self.assertEqual(result, 10)
    
    def test_n_8(self):
        """Test with n = 8, should return 92 solutions"""
        result = self.solution.totalNQueens(8)
        self.assertEqual(result, 92)


if __name__ == '__main__':
    unittest.main()