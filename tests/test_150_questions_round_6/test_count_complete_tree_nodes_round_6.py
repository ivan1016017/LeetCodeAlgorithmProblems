import unittest
from src.my_project.interviews.top_150_questions_round_6.\
count_complete_tree_nodes import TreeNode, Solution

class CountNodesTestCase(unittest.TestCase):

    def test_count_nodes(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.countNodes(tree)
        target = 3 
        self.assertEqual(output, target)