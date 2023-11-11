import unittest
from src.my_project.interviews.top_150_questions.\
same_tree_updated_updated_updated_updated import TreeNode, Solution

class SameTreeTestCase(unittest.TestCase):

    def test_diff_trees(self):
        solution = Solution()
        output = solution.isSameTree(p=TreeNode(1),q=TreeNode(2))
        self.assertFalse(output)

    def test_same_trees(self):
        solution = Solution()
        output = solution.isSameTree(p=(TreeNode(1,TreeNode(2),TreeNode(3))),
                                     q=(TreeNode(1,TreeNode(2),TreeNode(3))))
        self.assertTrue(output)
