import unittest
from src.my_project.interviews.top_150_questions_round_6.\
maximum_depth_tree import Solution, TreeNode

class MaxDepthTestCase(unittest.TestCase):

    def test_max_depth(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2))
        output = solution.maxDepth(root=tree)
        target = 2
        self.assertEqual(output, target)

    def test_max_depth_none(self):
        solution = Solution()
        tree = None
        output = solution.maxDepth(root=tree)
        target = 0
        self.assertEqual(output, target)