import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_145_maximal_square import Solution


class MaximumSquareTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        self.assertEqual(self.solution.maximalSquare(matrix), 4)

    def test_example_2(self):
        matrix = [["0", "1"], ["1", "0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 1)

    def test_example_3(self):
        matrix = [["0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 0)

    def test_all_ones(self):
        matrix = [["1", "1"], ["1", "1"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 4)


if __name__ == '__main__':
    unittest.main()
