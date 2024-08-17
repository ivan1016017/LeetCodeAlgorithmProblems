import unittest
from src.my_project.interviews.top_150_questions_round_8\
.count_nodes import TreeNode, Solution

class CountNodesTestCase(unittest.TestCase):

    def test_count_nodes(self):
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        target = 3 
        output = solution.countNodes(tree)
        self.assertEqual(output, target)