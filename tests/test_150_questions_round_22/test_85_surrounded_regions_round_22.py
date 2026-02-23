import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_85_surrounded_regions import Solution

class SurroundedRegionsTestCase(unittest.TestCase):

    def test_example_1(self):
        # Example 1: Board with surrounded regions
        # The O's in the center should be captured (converted to X)
        # The O on the bottom edge should not be captured
        solution = Solution()
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"]
        ]
        solution.solve(board)
        self.assertEqual(board, expected)

    def test_example_2(self):
        # Example 2: Single cell board
        solution = Solution()
        board = [["X"]]
        expected = [["X"]]
        solution.solve(board)
        self.assertEqual(board, expected)

