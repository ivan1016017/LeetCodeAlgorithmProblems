import unittest
from src.my_project.interviews.top_150_questions.\
climb_stairs_updated_updated_updated_updatd import Solution

class ClimbStairsTestCase(unittest.TestCase):

    def test_climb_stairs(self):
        solution = Solution()
        output = solution.climbStairs(n=3)
        self.assertEqual(output,3)