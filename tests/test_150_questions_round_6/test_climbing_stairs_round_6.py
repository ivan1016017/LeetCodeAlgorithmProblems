import unittest
from src.my_project.interviews.top_150_questions_round_6.\
climbing_stairs import Solution

class ClimbingStairsTestCase(unittest.TestCase):

    def test_climbing_stairs(self):
        solution = Solution()
        output = solution.climbStairs(n=3)
        target = 3
        self.assertEqual(output, target)