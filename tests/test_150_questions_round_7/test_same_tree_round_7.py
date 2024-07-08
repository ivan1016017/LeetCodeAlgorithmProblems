import unittest
from src.my_project.interviews.top_150_questions_round_7\
.same_tree import TreeNode, Solution

class SameTreeTestCase(unittest.TestCase):

    def test_is_same_tree(self):
        solution = Solution()
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.isSameTree(p=tree1, q=tree2)
        return self.assertTrue(output)
    
    def test_is_no_same_tree(self):
        solution = Solution()
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(3), TreeNode(2))
        output = solution.isSameTree(p=tree1, q=tree2)
        return self.assertFalse(output)