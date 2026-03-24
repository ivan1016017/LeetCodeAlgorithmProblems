import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_111_find_peak_element import Solution

class FindPeakElementTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_ascending_array(self):
        nums = [1, 2, 3, 1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 2)
    
    def test_multiple_peaks(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        result = self.solution.findPeakElement(nums)
        # Should return index of any peak (1 or 5)
        self.assertIn(result, [1, 5])
        # Verify it's actually a peak
        if result == 0:
            self.assertGreater(nums[result], nums[result + 1])
        elif result == len(nums) - 1:
            self.assertGreater(nums[result], nums[result - 1])
        else:
            self.assertGreater(nums[result], nums[result - 1])
            self.assertGreater(nums[result], nums[result + 1])
    
    def test_single_element(self):
        nums = [1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 0)
    
    def test_two_elements_ascending(self):
        nums = [1, 2]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 1)
    
    def test_two_elements_descending(self):
        nums = [2, 1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 0)
    
    def test_all_ascending(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 4)
    
    def test_all_descending(self):
        nums = [5, 4, 3, 2, 1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 0)