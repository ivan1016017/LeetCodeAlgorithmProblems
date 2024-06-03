import unittest
from src.my_project.interviews.top_150_questions_round_6.\
same_tree import TreeNode, Solution

class IsSameTreeTestCase(unittest.TestCase):

    def test_is_same(self):
        solution = Solution()
        tree1 = TreeNode(1)
        tree2 = TreeNode(1)
        output = solution.isSameTree(p=tree1, q=tree2)
        self.assertTrue(output)

    def test_is_no_same_case_1(self):
        solution = Solution()
        tree1 = TreeNode(1)
        tree2 = TreeNode(2)
        output = solution.isSameTree(p=tree1, q=tree2)
        self.assertFalse(output)

    def test_is_no_same_case_2(self):
        solution = Solution()
        tree1 = TreeNode(1)
        tree2 = None 
        output = solution.isSameTree(p=tree1, q=tree2)
        self.assertFalse(output)