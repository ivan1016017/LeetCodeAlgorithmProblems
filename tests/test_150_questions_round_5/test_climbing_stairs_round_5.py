import unittest
from src.my_project.interviews.top_150_questions_round_5.\
climbing_stairs  import Solution

class ClimbingStairsTestCase(unittest.TestCase):

    def test_climbing_stairs(self):
        solution = Solution()
        output = solution.climbStairs(n=2)
        target = 2 
        self.assertEqual(target, output)

def sample1():
    print('test1')