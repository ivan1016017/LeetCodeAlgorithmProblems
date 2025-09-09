import unittest
from src.my_project.interviews.top_150_questions_round_19\
.count_complete_nodes import Solution, TreeNode

class CountNodesTestCase(unittest.TestCase):

    def test_count_none(self):
        solution = Solution()
        tree = None 
        output = solution.countNodes(root=tree)
        self.assertEqual(0, output)


    def test_count_non_empty_tree(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.countNodes(root=tree)
        self.assertEqual(3, output)
