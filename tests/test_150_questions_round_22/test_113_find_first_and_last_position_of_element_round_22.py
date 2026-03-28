import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_113_find_first_and_last_position_of_element import Solution


class FindFirstAndLastPositionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1_target_exists_multiple_times(self):
        """Test: nums = [5,7,7,8,8,10], target = 8, expected = [3,4]"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_example_2_target_not_found(self):
        """Test: nums = [5,7,7,8,8,10], target = 6, expected = [-1,-1]"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_example_3_empty_array(self):
        """Test: nums = [], target = 0, expected = [-1,-1]"""
        nums = []
        target = 0
        expected = [-1, -1]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_single_element_found(self):
        """Test: nums = [1], target = 1, expected = [0,0]"""
        nums = [1]
        target = 1
        expected = [0, 0]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_single_element_not_found(self):
        """Test: nums = [1], target = 2, expected = [-1,-1]"""
        nums = [1]
        target = 2
        expected = [-1, -1]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_all_elements_same_as_target(self):
        """Test: nums = [2,2,2,2,2], target = 2, expected = [0,4]"""
        nums = [2, 2, 2, 2, 2]
        target = 2
        expected = [0, 4]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_target_at_beginning(self):
        """Test: nums = [1,1,1,2,3,4], target = 1, expected = [0,2]"""
        nums = [1, 1, 1, 2, 3, 4]
        target = 1
        expected = [0, 2]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_target_at_end(self):
        """Test: nums = [1,2,3,4,4,4], target = 4, expected = [3,5]"""
        nums = [1, 2, 3, 4, 4, 4]
        target = 4
        expected = [3, 5]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)
    
    def test_target_single_occurrence(self):
        """Test: nums = [1,2,3,4,5], target = 3, expected = [2,2]"""
        nums = [1, 2, 3, 4, 5]
        target = 3
        expected = [2, 2]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)