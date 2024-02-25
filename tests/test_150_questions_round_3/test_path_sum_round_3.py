import unittest
from src.my_project.interviews.top_150_questions_round_3.\
path_sum import TreeNode, Solution

class PathSumTestCase(unittest.TestCase):

    def test_none(self):
        solution = Solution()
        tree = None
        output = solution.hasPathSum(root=tree, targetSum=1)
        self.assertFalse(output)

    def test_has_path_sum(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.hasPathSum(root=tree, targetSum=3)
        self.assertTrue(output)

    def test_has_no_path_sum(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.hasPathSum(root=tree, targetSum=1)
        self.assertFalse(output)