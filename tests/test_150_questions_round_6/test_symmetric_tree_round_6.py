import unittest
from src.my_project.interviews.top_150_questions_round_6.\
symmetric_tree import TreeNode, Solution

class SymmetricTreeTestCase(unittest.TestCase):

    def test_is_symmetric(self):
        solution = Solution()
        output = solution.isSymmetric(TreeNode(1, TreeNode(7), TreeNode(7)))
        self.assertTrue(output)

    def test_is_no_symmetric(self):
        solution = Solution()
        output = solution.isSymmetric(TreeNode(1, TreeNode(2), TreeNode(3)))
        self.assertFalse(output)