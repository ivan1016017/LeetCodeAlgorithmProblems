import unittest
from src.my_project.interviews.top_150_questions_round_3.\
same_tree import TreeNode, Solution

class SameTreeTestCase(unittest.TestCase):

    def test_is_same_tree(self):
        solution = Solution()
        tree1 = TreeNode(1)
        tree2 = TreeNode(1)
        output = solution.isSameTree(p=tree1, q=tree2)
        self.assertTrue(output)

    def test_is_no_same_tree(self):
        solution = Solution()
        tree1 = TreeNode(1)
        tree2 = TreeNode(2)
        output = solution.isSameTree(p=tree1, q=tree2)
        self.assertFalse(output)