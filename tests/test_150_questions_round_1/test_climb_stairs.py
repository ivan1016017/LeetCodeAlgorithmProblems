import unittest
from src.my_project.interviews.top_150_questions_round_1.\
climb_stairs import Solution

class ClimbStairsTestCase(unittest.TestCase):

    def test_climb_stairs(self):
        solution = Solution()
        output = solution.climbStairs(5)
        self.assertEqual(8, output)