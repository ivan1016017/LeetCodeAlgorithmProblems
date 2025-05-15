import unittest
from src.my_project.interviews.top_150_questions_round_7\
.invert_binary_tree import TreeNode, Solution

class InvertTreeTestCase(unittest.TestCase):

    def test_binary_tree(self):
        solution = Solution()
        target = TreeNode(1, TreeNode(3), TreeNode(2))
        output = solution.invertTree(TreeNode(1, TreeNode(2), TreeNode(3)))
        self.assertEqual(target.val, output.val)
        self.assertEqual(target.left.val, output.left.val)
        self.assertEqual(target.right.val, output.right.val)