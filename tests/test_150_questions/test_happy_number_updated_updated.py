import unittest
from faker import Faker 
from src.my_project.interviews.top_150_questions.\
    happy_number_updated_updated_updated_updated import Solution

class HappyNumberTestCase(unittest.TestCase):

    def test_is_happy_number(self):
        solution = Solution()
        output = solution.isHappy(n=19)
        self.assertTrue(output)

    def test_is_no_happy_number(self):
        solution = Solution()
        output = solution.isHappy(n=3)
        self.assertFalse(output)