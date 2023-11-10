import unittest
from src.my_project.interviews.top_150_questions.\
maximum_depth_binary_tree_updated_updated_updated_updated import (TreeNode,
                                                                  Solution)


class DepthBinaryTreeTestCase(unittest.TestCase):

    def test_null_tree(self):
        solution = Solution()
        output = solution.maxDepth(root=None)
        self.assertEqual(output,0)

    def test_tree(self):
        solution = Solution()
        root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
        output = solution.maxDepth(root=root)
        self.assertEqual(output,3)