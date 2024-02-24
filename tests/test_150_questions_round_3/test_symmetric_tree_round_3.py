import unittest
from src.my_project.interviews.top_150_questions_round_3.\
symmetric_tree import TreeNode, Solution

class IsSymmetricTestCase(unittest.TestCase):

    def test_is_symmetric(self):
        solution = Solution()
        tree = TreeNode(1,2,2)
        output = solution.isSymmetric(root=tree)
        self.assertTrue(output)


    def test_is_no_symmetric_complete_tree(self):
        solution = Solution()
        tree = TreeNode(1,2,3)
        output = solution.isSymmetric(root=tree)
        self.assertFalse(output)

    def test_is_no_symmetric_incomplete_tree(self):
        solution = Solution()
        tree = TreeNode(1,2)
        output = solution.isSymmetric(root=tree)
        self.assertFalse(output)

    def test_none(self):
        solution = Solution()
        tree = None
        output = solution.isSymmetric(root=tree)
        self.assertTrue(output)
