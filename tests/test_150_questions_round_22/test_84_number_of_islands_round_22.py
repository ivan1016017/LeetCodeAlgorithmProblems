import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_84_number_of_islands import Solution

class NumberOfIslandsTescaseCase(unittest.TestCase):

    def test_example_1(self):
        # Example 1: Single island
        # Input: grid = [
        #   ["1","1","1","1","0"],
        #   ["1","1","0","1","0"],
        #   ["1","1","0","0","0"],
        #   ["0","0","0","0","0"]
        # ]
        # Output: 1
        solution = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        result = solution.numIslands(grid)
        self.assertEqual(result, 1)

    def test_example_2(self):
        # Example 2: Three islands
        # Input: grid = [
        #   ["1","1","0","0","0"],
        #   ["1","1","0","0","0"],
        #   ["0","0","1","0","0"],
        #   ["0","0","0","1","1"]
        # ]
        # Output: 3
        solution = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        result = solution.numIslands(grid)
        self.assertEqual(result, 3)

    def test_example_1_dfs(self):
        # Example 1: Single island (DFS approach)
        # Input: grid = [
        #   ["1","1","1","1","0"],
        #   ["1","1","0","1","0"],
        #   ["1","1","0","0","0"],
        #   ["0","0","0","0","0"]
        # ]
        # Output: 1
        solution = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        result = solution.numIslands_DFS(grid)
        self.assertEqual(result, 1)

    def test_example_2_dfs(self):
        # Example 2: Three islands (DFS approach)
        # Input: grid = [
        #   ["1","1","0","0","0"],
        #   ["1","1","0","0","0"],
        #   ["0","0","1","0","0"],
        #   ["0","0","0","1","1"]
        # ]
        # Output: 3
        solution = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        result = solution.numIslands_DFS(grid)
        self.assertEqual(result, 3)