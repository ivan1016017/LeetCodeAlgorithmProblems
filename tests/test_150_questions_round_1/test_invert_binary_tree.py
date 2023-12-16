import unittest
from src.my_project.interviews.top_150_questions_round_1.\
invert_binary_tree import TreeNode, Solution

class InvertTreeTestCase(unittest.TestCase):

    def test_invert_tree(self):
        solution = Solution()
        output = solution.invertTree(TreeNode(1,TreeNode(2),TreeNode(3)))
        self.assertEqual(1,output.val)
        self.assertEqual(3,output.left.val)
        self.assertEqual(2,output.right.val)