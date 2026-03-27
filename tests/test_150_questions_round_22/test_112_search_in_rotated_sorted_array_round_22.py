import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_112_search_in_rotated_sorted_array import Solution


class SearchInRotatedSortedArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test case from Example 1: target found at index 4"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_example_2(self):
        """Test case from Example 2: target not in array"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_example_3(self):
        """Test case from Example 3: single element, target not found"""
        nums = [1]
        target = 0
        expected = -1
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_single_element_found(self):
        """Test case: single element, target found"""
        nums = [1]
        target = 1
        expected = 0
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_no_rotation(self):
        """Test case: array not rotated"""
        nums = [1, 2, 3, 4, 5]
        target = 3
        expected = 2
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_rotation_at_beginning(self):
        """Test case: rotated at the beginning"""
        nums = [5, 1, 2, 3, 4]
        target = 1
        expected = 1
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_rotation_at_end(self):
        """Test case: rotated at the end"""
        nums = [2, 3, 4, 5, 1]
        target = 5
        expected = 3
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_target_at_beginning(self):
        """Test case: target is at the beginning"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 4
        expected = 0
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_target_at_end(self):
        """Test case: target is at the end"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2
        expected = 6
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_two_elements_rotated(self):
        """Test case: two elements rotated"""
        nums = [3, 1]
        target = 1
        expected = 1
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_two_elements_not_rotated(self):
        """Test case: two elements not rotated"""
        nums = [1, 3]
        target = 3
        expected = 1
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_larger_array(self):
        """Test case: larger rotated array"""
        nums = [10, 12, 14, 16, 18, 20, 2, 4, 6, 8]
        target = 18
        expected = 4
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_target_in_left_half(self):
        """Test case: target in left sorted portion"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 5
        expected = 1
        self.assertEqual(self.solution.search(nums, target), expected)
    
    def test_empty_array(self):
        """Test case: empty array"""
        nums = []
        target = 5
        expected = -1
        self.assertEqual(self.solution.search(nums, target), expected)
