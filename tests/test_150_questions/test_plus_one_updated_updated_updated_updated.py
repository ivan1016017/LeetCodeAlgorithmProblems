import unittest
from src.my_project.interviews.top_150_questions.\
plus_one_updated_updated_updated_updated import Solution

class PlusOneTestCase(unittest.TestCase):

    def test_with_no_leading_zero(self):
        solution = Solution()
        output = solution.plusOne(digits=[1,2,9])
        self.assertEqual([1,3,0],output)

    def test_with_leading_zero(self):
            solution = Solution()
            output = solution.plusOne(digits=[9,9,9])
            self.assertEqual([1,0,0,0],output)
