import unittest
from typing import List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_115_median_of_two_sorted_arrays import Solution


class MedianOfTwoSortedArraysTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1_odd_total_length(self):
        """Test: nums1 = [1,3], nums2 = [2], expected = 2.00000"""
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.00000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_example_2_even_total_length(self):
        """Test: nums1 = [1,2], nums2 = [3,4], expected = 2.50000"""
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.50000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_empty_nums1(self):
        """Test: nums1 = [], nums2 = [1], expected = 1.00000"""
        nums1 = []
        nums2 = [1]
        expected = 1.00000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_empty_nums2(self):
        """Test: nums1 = [2], nums2 = [], expected = 2.00000"""
        nums1 = [2]
        nums2 = []
        expected = 2.00000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_single_element_each_odd(self):
        """Test: nums1 = [1], nums2 = [2,3], expected = 2.00000"""
        nums1 = [1]
        nums2 = [2, 3]
        expected = 2.00000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_single_element_each_even(self):
        """Test: nums1 = [1], nums2 = [2], expected = 1.50000"""
        nums1 = [1]
        nums2 = [2]
        expected = 1.50000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_disjoint_arrays(self):
        """Test: nums1 = [1,2,3], nums2 = [4,5,6], expected = 3.50000"""
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        expected = 3.50000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_overlapping_arrays(self):
        """Test: nums1 = [1,3,5,7], nums2 = [2,4,6,8], expected = 4.50000"""
        nums1 = [1, 3, 5, 7]
        nums2 = [2, 4, 6, 8]
        expected = 4.50000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_negative_numbers(self):
        """Test: nums1 = [-5,-3,-1], nums2 = [-4,-2,0], expected = -2.50000"""
        nums1 = [-5, -3, -1]
        nums2 = [-4, -2, 0]
        expected = -2.50000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_mixed_positive_negative(self):
        """Test: nums1 = [-2,0], nums2 = [1,3], expected = 0.50000"""
        nums1 = [-2, 0]
        nums2 = [1, 3]
        expected = 0.50000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_duplicates(self):
        """Test: nums1 = [1,1], nums2 = [1,1], expected = 1.00000"""
        nums1 = [1, 1]
        nums2 = [1, 1]
        expected = 1.00000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_large_difference_in_sizes(self):
        """Test: nums1 = [1], nums2 = [2,3,4,5,6], expected = 3.50000"""
        nums1 = [1]
        nums2 = [2, 3, 4, 5, 6]
        expected = 3.50000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_all_elements_in_nums1_smaller(self):
        """Test: nums1 = [1,2], nums2 = [3,4,5], expected = 3.00000"""
        nums1 = [1, 2]
        nums2 = [3, 4, 5]
        expected = 3.00000
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(result, expected, places=5)