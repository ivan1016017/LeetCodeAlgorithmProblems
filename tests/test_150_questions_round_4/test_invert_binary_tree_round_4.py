import unittest
from src.my_project.interviews.top_150_questions_round_4.\
invert_binary_tree import TreeNode, Solution

class InvertBinaryTreeTestCase(unittest.TestCase):

    def test_non_null_binary_tree(self):
        solution = Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3))
        output = solution.invertTree(root=tree)
        self.assertEqual(1, output.val)
        self.assertEqual(2, output.right.val)
        self.assertEqual(3, output.left.val)

    def test_none_inverted_tree(self):
        solution = Solution()
        tree = None
        output = solution.invertTree(root=tree)
        self.assertIsNone(output)