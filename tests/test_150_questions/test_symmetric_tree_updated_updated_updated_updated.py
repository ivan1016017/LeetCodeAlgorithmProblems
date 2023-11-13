import unittest
from src.my_project.interviews.top_150_questions.\
symmetric_tree_updated_updated_updated_updated import (TreeNode, Solution)

class SymmetricTreeTestCase(unittest.TestCase):

    def test_both_none(self):
        solution = Solution()
        output = solution.isSymmetric(root=None)
        self.assertTrue(output)

    def test_none_and_not_none(self):
        root = TreeNode(val=1,left=TreeNode(val=1),right=None)
        solution = Solution()
        output = solution.isSymmetric(root=root)
        self.assertFalse(output)

    def test_symmetric(self):
        root = TreeNode(val=1,left=TreeNode(val=2,left=TreeNode(3)),right=TreeNode(2,right=TreeNode(3)))
        solution = Solution()
        output = solution.isSymmetric(root=root)
        self.assertTrue(output)
        
        