import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_97_combinations import Solution


class CombinationsTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # n = 4, k = 2
        result = self.solution.combine(4, 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_2(self):
        # n = 1, k = 1
        result = self.solution.combine(1, 1)
        expected = [[1]]
        self.assertEqual(result, expected)
    
    def test_k_equals_n(self):
        # When k equals n, there's only one combination
        result = self.solution.combine(3, 3)
        expected = [[1, 2, 3]]
        self.assertEqual(result, expected)
    
    def test_k_equals_1(self):
        # When k = 1, each number is a combination
        result = self.solution.combine(3, 1)
        expected = [[1], [2], [3]]
        self.assertEqual(result, expected)
    
    def test_larger_case(self):
        # n = 5, k = 3
        result = self.solution.combine(5, 3)
        # Should have 5C3 = 10 combinations
        self.assertEqual(len(result), 10)
        # Verify all combinations are unique
        self.assertEqual(len(result), len(set(map(tuple, result))))
        # Verify all elements are in correct range
        for combo in result:
            self.assertEqual(len(combo), 3)
            for num in combo:
                self.assertTrue(1 <= num <= 5)
            # Verify combination is sorted (which it should be from our algorithm)
            self.assertEqual(combo, sorted(combo))