import unittest
from src.my_project.interviews.top_150_questions_round_21\
.permutations import Solution

class PermutationTestCase(unittest.TestCase):

    def test_permutation_1(self):
        solution = Solution()
        output = solution.permute(nums = [1,2,3])
        target = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(output, target)