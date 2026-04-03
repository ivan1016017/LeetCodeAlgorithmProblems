import unittest
from typing import List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_118_find_k_pairs_with_smallest_sums import Solution


class FindKPairsWithSmallestSumsTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test: nums1=[1,7,11], nums2=[2,4,6], k=3, expected=[[1,2],[1,4],[1,6]]"""
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 3
        expected = [[1, 2], [1, 4], [1, 6]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test: nums1=[1,1,2], nums2=[1,2,3], k=2, expected=[[1,1],[1,1]]"""
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 2
        expected = [[1, 1], [1, 1]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_k_equals_total_pairs(self):
        """Test: k equals total number of pairs"""
        nums1 = [1, 2]
        nums2 = [3, 4]
        k = 4
        expected = [[1, 3], [1, 4], [2, 3], [2, 4]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_single_element_each(self):
        """Test: nums1=[1], nums2=[2], k=1, expected=[[1,2]]"""
        nums1 = [1]
        nums2 = [2]
        k = 1
        expected = [[1, 2]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_k_larger_than_nums1(self):
        """Test: k larger than len(nums1), uses all nums1 elements initially"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        k = 4
        expected = [[1, 1], [1, 2], [2, 1], [1, 3]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(sorted(result), sorted(expected))

    def test_negative_numbers(self):
        """Test: arrays contain negative numbers"""
        nums1 = [-4, -2, 0]
        nums2 = [-3, -1, 2]
        k = 3
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(len(result), 3)
        sums = [pair[0] + pair[1] for pair in result]
        self.assertEqual(sums, sorted(sums))

    def test_k_equals_1(self):
        """Test: k=1 returns only the pair with the smallest sum"""
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 1
        expected = [[1, 2]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)
