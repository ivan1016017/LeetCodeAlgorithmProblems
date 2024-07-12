import unittest
from src.my_project.interviews.top_150_questions_round_7.\
count_complete_nodes import TreeNode, Solution

class CountCompleteNodesTestCase(unittest.TestCase):

    def test_count_none_tree(self):
        solution = Solution()
        output = solution.countNodes(None)
        target = 0 
        self.assertEqual(output, target)

    def test_count_none_empty_tree(self):
        solution = Solution()
        output = solution.countNodes(TreeNode(1, TreeNode(2)))
        target = 2 
        self.assertEqual(output, target)