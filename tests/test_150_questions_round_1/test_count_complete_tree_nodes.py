import unittest
from src.my_project.interviews.top_150_questions_round_1.\
count_complete_tree_nodes import TreeNode, Solution

class CountCompleteTreeNodesTestCase(unittest.TestCase):

    def test_none_tree(self):
        solution = Solution()
        tree = None 
        output = solution.countNodes(root=tree)
        self.assertEqual(0,output)

    def test_count_complete_nodes(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3)) 
        output = solution.countNodes(root=tree)
        self.assertEqual(3,output)

    def test_count_single_complete_nodes(self):
        solution = Solution()
        tree = TreeNode(1) 
        output = solution.countNodes(root=tree)
        self.assertEqual(1,output)

    

