import unittest
from src.my_project.interviews.top_150_questions_round_5.\
path_sum import TreeNode, Solution

class PathSumTestCase(unittest.TestCase):

    def test_is_path_sum(self):
        solution = Solution()
        output = solution.hasPathSum(TreeNode(1,TreeNode(2),TreeNode(3)), 4)
        self.assertTrue(output)

    def test_is_no_path_sum(self):
        solution = Solution()
        output = solution.hasPathSum(TreeNode(1,TreeNode(2),TreeNode(3)), 10)
        self.assertFalse(output)

def testing_one():
    pass 

def testing_two():
    pass 
