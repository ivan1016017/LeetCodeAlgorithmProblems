import unittest
from src.my_project.interviews.top_150_questions_round_15\
.path_sum import TreeNode, Solution

class HasPathSumTestCase(unittest.TestCase):

    def test_is_path_sum(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.hasPathSum(root=tree, targetSum=3)
        self.assertTrue(output)

    def test_is_no_path_sum(self):
            solution = Solution()
            tree = TreeNode(1, TreeNode(2), TreeNode(3))
            output = solution.hasPathSum(root=tree, targetSum=10)
            self.assertFalse(output)