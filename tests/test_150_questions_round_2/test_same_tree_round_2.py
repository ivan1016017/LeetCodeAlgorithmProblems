import unittest 
from src.my_project.interviews.top_150_questions_round_2.\
same_tree import TreeNode, Solution

class SameTreeTestCase(unittest.TestCase):

    def test_is_same_tree(self):
        solution = Solution()
        tree_1 = TreeNode(1)
        tree_2 = TreeNode(1)
        output = solution.isSameTree(p=tree_1, q=tree_2)
        self.assertTrue(output)

    def test_is_no_same_tree(self):
        solution = Solution()
        tree_1 = TreeNode(1)
        tree_2 = TreeNode(2)
        output = solution.isSameTree(p=tree_1, q=tree_2)
        self.assertFalse(output)