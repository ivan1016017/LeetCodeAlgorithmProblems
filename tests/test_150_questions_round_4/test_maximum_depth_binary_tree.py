import unittest
from src.my_project.interviews.top_150_questions_round_4.\
maximum_depth_binary_tree import Solution, TreeNode

class MaxDepthTestCase(unittest.TestCase):

    def test_null_tree(self):
        solution = Solution()
        tree = None
        output = solution.maxDepth(root=tree)
        self.assertEqual(0, output)

    def test_non_null_tree(self):
        solution = Solution()
        tree = TreeNode(1)
        output = solution.maxDepth(root=tree)
        self.assertEqual(1, output)