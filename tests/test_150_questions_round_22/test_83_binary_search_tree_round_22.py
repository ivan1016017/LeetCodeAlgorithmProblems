import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_83_binary_search_tree import Solution, TreeNode

class BinarySearchTreeTestCase(unittest.TestCase):

    def create_binary_tree(self, values):
        """
        Helper function to create a binary tree from a list of values (level-order).
        
        :param values: List of node values (None represents null nodes)
        :return: Root of the binary tree
        """
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root

    def test_example_1(self):
        # Example 1: Input: root = [2,1,3]
        # Output: true
        solution = Solution()
        root = self.create_binary_tree([2, 1, 3])
        result = solution.isValidBST(root)
        self.assertTrue(result)

    def test_example_2(self):
        # Example 2: Input: root = [5,1,4,null,null,3,6]
        # Output: false
        # Explanation: The root node's value is 5 but its right child's value is 4.
        solution = Solution()
        root = self.create_binary_tree([5, 1, 4, None, None, 3, 6])
        result = solution.isValidBST(root)
        self.assertFalse(result)