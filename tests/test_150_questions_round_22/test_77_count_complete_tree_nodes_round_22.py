import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_77_count_complete_tree_nodes import Solution, TreeNode


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