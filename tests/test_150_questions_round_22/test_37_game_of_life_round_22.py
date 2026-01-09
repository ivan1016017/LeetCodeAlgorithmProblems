import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_37_game_of_life import Solution

class GameOfLifeTestCase(unittest.TestCase):

    def test_first_pattern(self):
        solution = Solution()
        output = solution.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
        target = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        self.assertEqual(output, target)

    def test_second_pattern(self):
        solution = Solution()
        output = solution.gameOfLife(board = [[1,1],[1,0]])
        target = [[1,1],[1,1]]
        self.assertEqual(output, target)
