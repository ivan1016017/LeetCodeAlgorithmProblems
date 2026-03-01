import unittest
from src.my_project.interviews.top_150_questions_round_22\
    .ex_90_snakes_and_ladders import Solution
from typing import Optional, List


class SnakesAndLaddersTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Example 1:
        Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
        Output: 4
        Explanation: 
        In the beginning, you start at square 1 (at row 5, column 0).
        You decide to move to square 2 and must take the ladder to square 15.
        You then decide to move to square 17 and must take the snake to square 13.
        You then decide to move to square 14 and must take the ladder to square 35.
        You then decide to move to square 36, ending the game.
        This is the lowest possible number of moves to reach the last square, so return 4.
        """
        solution = Solution()
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1]
        ]
        expected = 4
        
        result = solution.snakesAndLadders(board)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """
        Example 2:
        Input: board = [[-1,-1],[-1,3]]
        Output: 1
        """
        solution = Solution()
        board = [[-1, -1], [-1, 3]]
        expected = 1
        
        result = solution.snakesAndLadders(board)
        self.assertEqual(result, expected)

