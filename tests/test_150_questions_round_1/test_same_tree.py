import unittest
from src.my_project.interviews.top_150_questions_round_1.\
same_tree import TreeNode, Solution

class IsSameTreeTestCase(unittest.TestCase):

    def test_is_no_same_tree(self):
        solution = Solution()
        tree1 = TreeNode(1)
        tree2 = TreeNode(2)
        output = solution.isSameTree(tree1,tree2)
        self.assertFalse(output)

    def test_is_same_tree(self):
        solution = Solution()
        tree1 = TreeNode(1,TreeNode(2),TreeNode(3))
        tree2 = TreeNode(1,TreeNode(2),TreeNode(3))
        output = solution.isSameTree(tree1,tree2)
        self.assertTrue(output)