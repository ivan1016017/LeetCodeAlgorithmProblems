import unittest
from src.my_project.interviews.top_150_questions_round_22\
    .ex_87_evaluate_division import Solution
from typing import Optional, List


class EvaluateDivisionTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Example 1: Basic division chain
        Given: a / b = 2.0, b / c = 3.0
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
        return: [6.0, 0.5, -1.0, 1.0, -1.0]
        """
        solution = Solution()
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        
        result = solution.calcEquation(equations, values, queries)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """
        Example 2: Multiple variables and chains
        Given: a / b = 1.5, b / c = 2.5, bc / cd = 5.0
        queries are: a / c = ?, c / b = ?, bc / cd = ?, cd / bc = ?
        return: [3.75, 0.4, 5.0, 0.2]
        """
        solution = Solution()
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75, 0.4, 5.0, 0.2]
        
        result = solution.calcEquation(equations, values, queries)
        self.assertEqual(result, expected)

    def test_example_3(self):
        """
        Example 3: Single equation with various queries
        Given: a / b = 0.5
        queries are: a / b = ?, b / a = ?, a / c = ?, x / y = ?
        return: [0.5, 2.0, -1.0, -1.0]
        """
        solution = Solution()
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.5, 2.0, -1.0, -1.0]
        
        result = solution.calcEquation(equations, values, queries)
        self.assertEqual(result, expected)

