import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_96_letter_of_combinations_of_a_phone_number import Solution


class LetterOfCombinationsOfAPhoneNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        digits = "23"
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_2(self):
        digits = "2"
        expected = ["a","b","c"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_empty_string(self):
        digits = ""
        expected = []
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, expected)
    
    def test_single_digit_9(self):
        digits = "9"
        expected = ["w", "x", "y", "z"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_three_digits(self):
        digits = "234"
        # Should have 3 * 3 * 3 = 27 combinations
        result = self.solution.letterCombinations(digits)
        self.assertEqual(len(result), 27)
        self.assertIn("adg", result)
        self.assertIn("bfi", result)
        self.assertIn("cfi", result)