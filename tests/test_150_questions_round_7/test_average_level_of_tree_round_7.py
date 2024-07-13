import unittest
from src.my_project.interviews.top_150_questions_round_7.\
average_level_of_tree import TreeNode, Solution

class AverageLevelsTreeTestCase(unittest.TestCase):

    def test_average_level(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(3), TreeNode(5))
        output = solution.averageOfLevels(tree)
        target = [1,4]
        for k, v in enumerate(target):
            self.assertEqual(output[k], v)