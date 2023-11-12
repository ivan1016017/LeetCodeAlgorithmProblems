import unittest
from src.my_project.interviews.top_150_questions.\
invert_tree_updated_updated_updated_updated import (TreeNode, Solution)

class InvertBinaryTreeTestCase(unittest.TestCase):

    def test_null_tree(self):
        solution = Solution()
        output = solution.invertTree(root=None)
        self.assertIsNone(output)

    def test_non_null_tree(self):
        solution = Solution()
        input = TreeNode(val=1,left=TreeNode(val=2),right=TreeNode(val=3))
        check = TreeNode(val=1,left=TreeNode(val=3),right=TreeNode(val=2))
        output = solution.invertTree(root=input)
        self.assertEqual(output.val,check.val)
        self.assertEqual(output.left.val,check.left.val)
        self.assertEqual(output.right.val,check.right.val)
