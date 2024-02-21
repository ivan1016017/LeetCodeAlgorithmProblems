import unittest
from src.my_project.interviews.top_150_questions_round_3.\
maximum_depth_of_binary_tree import Solution, TreeNode

class MaxDepthTestCase(unittest.TestCase):

    def test_max_depth_non_empty_binary_tree(self):
        solution = Solution()
        tree = TreeNode(1)
        output = solution.maxDepth(root=tree)
        self.assertEqual(1, output)

    def test_max_depth_empty_binary_tree(self):
        solution = Solution()
        tree = None
        output = solution.maxDepth(root=tree)
        self.assertEqual(0, output)