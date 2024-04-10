import unittest
from src.my_project.interviews.top_150_questions_round_4.\
climbing_stairs import Solution

class ClimbStairsTestCase(unittest.TestCase):

    def test_climbing_stairs(self):
        solution = Solution()
        input = 3
        target = 3
        output = solution.climbStairs(n=input)
        self.assertEqual(target, output)