import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_98_permutations import Solution


class PermutationsTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1_three_elements(self):
        """Test with three distinct integers"""
        nums = [1, 2, 3]
        result = self.solution.permute(nums)
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(len(result), len(expected))
        for perm in expected:
            self.assertIn(perm, result)
    
    def test_example_2_two_elements(self):
        """Test with two distinct integers"""
        nums = [0, 1]
        result = self.solution.permute(nums)
        expected = [[0, 1], [1, 0]]
        self.assertEqual(len(result), len(expected))
        for perm in expected:
            self.assertIn(perm, result)
    
    def test_example_3_single_element(self):
        """Test with single integer"""
        nums = [1]
        result = self.solution.permute(nums)
        expected = [[1]]
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-1, 0, 1]
        result = self.solution.permute(nums)
        expected = [[-1, 0, 1], [-1, 1, 0], [0, -1, 1], [0, 1, -1], [1, -1, 0], [1, 0, -1]]
        self.assertEqual(len(result), len(expected))
        for perm in expected:
            self.assertIn(perm, result)
    
    def test_four_elements(self):
        """Test with four elements"""
        nums = [1, 2, 3, 4]
        result = self.solution.permute(nums)
        # 4! = 24 permutations
        self.assertEqual(len(result), 24)
        # Check all permutations are unique
        unique_perms = [tuple(perm) for perm in result]
        self.assertEqual(len(set(unique_perms)), 24)
        # Check each permutation contains all original numbers
        for perm in result:
            self.assertEqual(sorted(perm), sorted(nums))
    
    def test_five_elements(self):
        """Test with five elements"""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.permute(nums)
        # 5! = 120 permutations
        self.assertEqual(len(result), 120)
        # Check all permutations are unique
        unique_perms = [tuple(perm) for perm in result]
        self.assertEqual(len(set(unique_perms)), 120)
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        nums = [-2, 3]
        result = self.solution.permute(nums)
        expected = [[-2, 3], [3, -2]]
        self.assertEqual(len(result), len(expected))
        for perm in expected:
            self.assertIn(perm, result)
    
    def test_zero_and_negatives(self):
        """Test with zero and negative numbers"""
        nums = [0, -1]
        result = self.solution.permute(nums)
        expected = [[0, -1], [-1, 0]]
        self.assertEqual(len(result), len(expected))
        for perm in expected:
            self.assertIn(perm, result)