import unittest
from typing import List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_114_find_minimum_in_rotated_sorted_array import Solution


class FindMinimumInRotatedSortedArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1_rotated_3_times(self):
        """Test: nums = [3,4,5,1,2], expected = 1"""
        nums = [3, 4, 5, 1, 2]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_example_2_rotated_4_times(self):
        """Test: nums = [4,5,6,7,0,1,2], expected = 0"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_example_3_no_rotation_or_full_rotation(self):
        """Test: nums = [11,13,15,17], expected = 11"""
        nums = [11, 13, 15, 17]
        expected = 11
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_single_element(self):
        """Test: nums = [1], expected = 1"""
        nums = [1]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_two_elements_rotated(self):
        """Test: nums = [2,1], expected = 1"""
        nums = [2, 1]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_two_elements_not_rotated(self):
        """Test: nums = [1,2], expected = 1"""
        nums = [1, 2]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_minimum_at_beginning(self):
        """Test: nums = [1,2,3,4,5], expected = 1"""
        nums = [1, 2, 3, 4, 5]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_minimum_at_end(self):
        """Test: nums = [2,3,4,5,1], expected = 1"""
        nums = [2, 3, 4, 5, 1]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_minimum_in_middle(self):
        """Test: nums = [5,6,7,1,2,3,4], expected = 1"""
        nums = [5, 6, 7, 1, 2, 3, 4]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
    
    def test_large_rotation(self):
        """Test: nums = [6,7,8,9,10,1,2,3,4,5], expected = 1"""
        nums = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
        expected = 1
        result = self.solution.findMin(nums)
        self.assertEqual(result, expected)
