import unittest
from src.my_project.interviews.top_150_questions_round_5.\
same_tree import TreeNode, Solution

class SameTreeTestCase(unittest.TestCase):

    def test_same_tree(self):
        solution = Solution()
        p = TreeNode(1)
        q = TreeNode(1)
        output = solution.isSameTree(p, q)
        self.assertTrue(output)

    def test_no_same_tree(self):
        solution = Solution()
        p = TreeNode(1)
        q = None
        output = solution.isSameTree(p, q)
        self.assertFalse(output)

def sample():
    print('testing feature')