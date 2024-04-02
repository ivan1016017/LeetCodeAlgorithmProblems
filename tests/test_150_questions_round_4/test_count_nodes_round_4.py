import unittest
from src.my_project.interviews.top_150_questions_round_4.\
count_nodes import TreeNode, Solution

class CountNodesTestCase(unittest.TestCase):

    def test_count_nodes_non_empty_tree(self):
        solution = Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3))
        output = solution.countNodes(tree)
        self.assertEqual(3, output)


    def test_count_nodes_empty_tree(self):
        solution = Solution()
        tree = None
        output = solution.countNodes(tree)
        self.assertEqual(0, output)