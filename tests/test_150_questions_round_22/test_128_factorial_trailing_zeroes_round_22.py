import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_128_factorial_trailing_zeroes import Solution

class FactorialTrailingZeroesTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # 3! = 6, no trailing zero
        self.assertEqual(self.solution.trailingZeroes(3), 0)
    
    def test_example_2(self):
        # 5! = 120, one trailing zero
        self.assertEqual(self.solution.trailingZeroes(5), 1)
    
    def test_example_3(self):
        # 0! = 1, no trailing zero
        self.assertEqual(self.solution.trailingZeroes(0), 0)
    
    def test_larger_number(self):
        # 10! = 3628800, two trailing zeroes
        self.assertEqual(self.solution.trailingZeroes(10), 2)
    
    def test_multiple_of_25(self):
        # 25! has floor(25/5) + floor(25/25) = 5 + 1 = 6 trailing zeroes
        self.assertEqual(self.solution.trailingZeroes(25), 6)
    
    def test_large_number(self):
        # 100! has many trailing zeroes
        # floor(100/5) + floor(100/25) + floor(100/125) = 20 + 4 + 0 = 24
        self.assertEqual(self.solution.trailingZeroes(100), 24)
    
    def test_single_digit(self):
        # 4! = 24, no trailing zero
        self.assertEqual(self.solution.trailingZeroes(4), 0)


if __name__ == "__main__":
    unittest.main()
