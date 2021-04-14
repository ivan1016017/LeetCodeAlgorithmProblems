import unittest
from src.my_project.easy_problems.from1to50.factorial_trailing_zeroes import Solution
import random
from faker import Faker


class FactorialTrailingZeroesTestCase(unittest.TestCase):


    def test_one_zero(self):
        solution = Solution()
        self.assertEqual(solution.trailingZeroes(5),1)

    def test_two_zero(self):
        solution = Solution()
        self.assertEqual(solution.trailingZeroes(10),2)