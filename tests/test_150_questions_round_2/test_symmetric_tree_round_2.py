import unittest
from src.my_project.interviews.top_150_questions_round_2.\
symmetric_tree import TreeNode, Solution

class SymmetricTreeTestCase(unittest.TestCase):

    def test_is_symmetric(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(2))
        output = solution.isSymmetric(tree)
        self.assertTrue(output)

    def test_is_no_symmetric(self):
            solution = Solution()
            tree = TreeNode(1, TreeNode(2), TreeNode(3))
            output = solution.isSymmetric(tree)
            self.assertFalse(output)

    def test_is_none_symmetric(self):
            solution = Solution()
            tree = None
            output = solution.isSymmetric(tree)
            self.assertTrue(output)