import unittest
from src.my_project.interviews.top_150_questions_round_3.\
average_levels_binary_tree import TreeNode, Solution

class AverageLevelBinaryTreeTestCase(unittest.TestCase):

    def test_level_binary_tree(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(3), TreeNode(4))
        output = solution.averageOfLevels(root=tree)
        self.assertEqual(1, output[0])
        self.assertEqual(3.5, output[1])