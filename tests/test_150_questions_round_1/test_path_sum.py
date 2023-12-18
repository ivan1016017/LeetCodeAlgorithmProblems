import unittest
from src.my_project.interviews.top_150_questions_round_1.\
path_sum import TreeNode, Solution

class PathSumTestCase(unittest.TestCase):

    def test_none(self):
        solution = Solution()
        tree = None 
        target = 5
        output = solution.hasPathSum(root=tree, targetSum=target)
        self.assertFalse(output)

    def test_path_sum(self):
        solution = Solution()
        tree = TreeNode(2,TreeNode(3),TreeNode(4))
        target = 5
        output = solution.hasPathSum(root=tree, targetSum=target)
        self.assertTrue(output)