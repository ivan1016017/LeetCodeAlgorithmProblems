import unittest
from src.my_project.interviews.top_150_questions_round_8\
.max_depth_tree import Solution, TreeNode

class MaxDepthTreeTestCase(unittest.TestCase):

    def test_max_depth_null(self):
        solution = Solution()
        tree = None
        output = solution.maxDepth(root=tree)
        target = 0
        self.assertEqual(output, target)

    def test_max_depth(self):
        solution = Solution()
        tree = TreeNode(1)
        output = solution.maxDepth(root=tree)
        target = 1
        self.assertEqual(output, target)