import unittest
from src.my_project.interviews.top_150_questions_round_1.\
average_level_binary_tree import TreeNode, Solution

class AverageLevelBinaryTreeTestCase(unittest.TestCase):

    def test_average_level_tree(self):
        solution = Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3))
        output = solution.averageOfLevels(root=tree)
        self.assertEqual(1, output[0])
        self.assertEqual(2.5, output[1])
