import unittest
from src.my_project.interviews.top_150_questions_round_5.\
max_depth_binary_tree import Solution, TreeNode

class MaxDepthBinaryTreeTestCase(unittest.TestCase):

    def test_none_binary_tree(self):
        solution = Solution()
        target = 0
        output = solution.maxDepth(root=None)
        self.assertEqual(target, output)

    def test_binary_tree(self):
        solution = Solution()
        target = 2
        output = solution.maxDepth(root=TreeNode(1, TreeNode(2), TreeNode(3)))
        self.assertEqual(target, output)