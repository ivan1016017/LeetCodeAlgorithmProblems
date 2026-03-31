import unittest
from typing import List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_116_kth_largest_element_in_array import Solution


class KthLargestElementTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test: nums = [3,2,1,5,6,4], k = 2, expected = 5"""
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 5)

    def test_example_2(self):
        """Test: nums = [3,2,3,1,2,4,5,5,6], k = 4, expected = 4"""
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 4)

    def test_single_element(self):
        """Test: nums = [1], k = 1, expected = 1"""
        nums = [1]
        k = 1
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 1)

    def test_all_same_elements(self):
        """Test: nums = [3,3,3,3], k = 2, expected = 3"""
        nums = [3, 3, 3, 3]
        k = 2
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 3)

    def test_k_equals_length(self):
        """Test: nums = [7,6,5,4,3,2,1], k = 7, expected = 1"""
        nums = [7, 6, 5, 4, 3, 2, 1]
        k = 7
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 1)

    def test_k_equals_1(self):
        """Test: nums = [2,1,4,3], k = 1, expected = 4"""
        nums = [2, 1, 4, 3]
        k = 1
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """Test: nums = [-1,-2,-3,-4], k = 2, expected = -2"""
        nums = [-1, -2, -3, -4]
        k = 2
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, -2)

    def test_duplicates_with_target(self):
        """Test: nums = [1,2,2,3,3,4], k = 3, expected = 3"""
        nums = [1, 2, 2, 3, 3, 4]
        k = 3
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 3)

    def test_two_elements(self):
        """Test: nums = [2,1], k = 1, expected = 2"""
        nums = [2, 1]
        k = 1
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result, 2)