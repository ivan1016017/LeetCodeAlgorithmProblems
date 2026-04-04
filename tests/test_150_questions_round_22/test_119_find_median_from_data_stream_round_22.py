import unittest
from typing import List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_119_find_median_from_data_stream import MedianFinder

class MedianFromDataStreamTestCase(unittest.TestCase):
    def test_example_1_sequence(self):
        """Test: Example 1 from problem description"""
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5, places=5)
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0, places=5)
    
    def test_single_element(self):
        """Test: Single element should return that element"""
        mf = MedianFinder()
        mf.addNum(5)
        self.assertAlmostEqual(mf.findMedian(), 5.0, places=5)
    
    def test_two_elements(self):
        """Test: Two elements should return their average"""
        mf = MedianFinder()
        mf.addNum(10)
        mf.addNum(20)
        self.assertAlmostEqual(mf.findMedian(), 15.0, places=5)
    
    def test_odd_number_of_elements(self):
        """Test: Odd count should return middle element"""
        mf = MedianFinder()
        for num in [1, 2, 3, 4, 5]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), 3.0, places=5)
    
    def test_even_number_of_elements(self):
        """Test: Even count should return average of two middle elements"""
        mf = MedianFinder()
        for num in [1, 2, 3, 4]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), 2.5, places=5)
    
    def test_unsorted_input(self):
        """Test: Numbers added in random order"""
        mf = MedianFinder()
        for num in [5, 15, 1, 3]:
            mf.addNum(num)
        # Sorted: [1, 3, 5, 15] -> median = (3 + 5) / 2 = 4.0
        self.assertAlmostEqual(mf.findMedian(), 4.0, places=5)
    
    def test_duplicate_values(self):
        """Test: Handle duplicate values correctly"""
        mf = MedianFinder()
        for num in [5, 5, 5, 5]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), 5.0, places=5)
    
    def test_negative_numbers(self):
        """Test: Handle negative numbers"""
        mf = MedianFinder()
        for num in [-1, -2, -3]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), -2.0, places=5)
    
    def test_mixed_positive_negative(self):
        """Test: Mix of positive and negative numbers"""
        mf = MedianFinder()
        for num in [-5, -1, 0, 3, 5]:
            mf.addNum(num)
        self.assertAlmostEqual(mf.findMedian(), 0.0, places=5)
    
    def test_large_range(self):
        """Test: Numbers with large range"""
        mf = MedianFinder()
        mf.addNum(-100000)
        mf.addNum(100000)
        self.assertAlmostEqual(mf.findMedian(), 0.0, places=5)
    
    def test_sequential_medians(self):
        """Test: Verify median after each addition"""
        mf = MedianFinder()
        mf.addNum(1)
        self.assertAlmostEqual(mf.findMedian(), 1.0, places=5)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5, places=5)
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0, places=5)
        mf.addNum(4)
        self.assertAlmostEqual(mf.findMedian(), 2.5, places=5)
        mf.addNum(5)
        self.assertAlmostEqual(mf.findMedian(), 3.0, places=5)