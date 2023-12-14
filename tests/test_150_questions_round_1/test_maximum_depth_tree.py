import unittest
from src.my_project.interviews.top_150_questions_round_1.\
maximum_depth_tree import TreeNode, Solution

class MaximumDepthTreeTestCase(unittest.TestCase):

    def test_depth_none(self):
        solution = Solution()
        output = solution.maxDepth(root=None)
        self.assertEqual(0,output)


    def test_depth_tree(self):
        solution = Solution()
        output = solution.maxDepth(TreeNode(1,TreeNode(2),TreeNode(3)))
        self.assertEqual(2,output)