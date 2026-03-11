import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_99_combination_sum import Solution


class CombinationSumTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        """Test case: candidates = [2,3,6,7], target = 7"""
        candidates = [2, 3, 6, 7]
        target = 7
        result = self.solution.combinationSum(candidates, target)
        expected = [[2, 2, 3], [7]]
        self.assertEqual(sorted([sorted(x) for x in result]), 
                        sorted([sorted(x) for x in expected]))
    
    def test_example2(self):
        """Test case: candidates = [2,3,5], target = 8"""
        candidates = [2, 3, 5]
        target = 8
        result = self.solution.combinationSum(candidates, target)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(sorted([sorted(x) for x in result]), 
                        sorted([sorted(x) for x in expected]))
    
    def test_example3(self):
        """Test case: candidates = [2], target = 1"""
        candidates = [2]
        target = 1
        result = self.solution.combinationSum(candidates, target)
        expected = []
        self.assertEqual(result, expected)
    
    def test_single_element_exact(self):
        """Test case: single element that equals target"""
        candidates = [5]
        target = 5
        result = self.solution.combinationSum(candidates, target)
        expected = [[5]]
        self.assertEqual(result, expected)
    
    def test_multiple_use_same_number(self):
        """Test case: using same number multiple times"""
        candidates = [3]
        target = 9
        result = self.solution.combinationSum(candidates, target)
        expected = [[3, 3, 3]]
        self.assertEqual(result, expected)