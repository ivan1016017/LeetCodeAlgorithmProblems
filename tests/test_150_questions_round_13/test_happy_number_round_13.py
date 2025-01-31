import unittest
from src.my_project.interviews.top_150_questions_round_13\
.happy_number import Solution

class HappyNumberTestCase(unittest.TestCase):

    def test_is_happy_number(self):
        solution = Solution()
        output = solution.isHappy(n=19)
        self.assertTrue(output)

    def test_is_no_happy_number(self):
        solution = Solution()
        output = solution.isHappy(n=2)
        self.assertFalse(output)