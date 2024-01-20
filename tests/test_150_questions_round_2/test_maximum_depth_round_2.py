import unittest
from src.my_project.interviews.top_150_questions_round_2.\
maximum_depth import TreeNode, Solution

class MaximumDepthTestCase(unittest.TestCase):

    def test_maximum_depth_null(self):
        solution = Solution()
        tree = None 
        output = solution.maxDepth(tree)
        self.assertEqual(0, output)

    def test_maximum_depth(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.maxDepth(tree)
        self.assertEqual(2, output)