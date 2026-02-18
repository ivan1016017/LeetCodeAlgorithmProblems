import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_80_average_of_levels_in_binary_tree import Solution, TreeNode

class AverageOfLevelsInBinaryTreeTestCase(unittest.TestCase):

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
        # Example 1: Input: root = [3,9,20,null,null,15,7]
        # Output: [3.00000,14.50000,11.00000]
        # Explanation: The average value of nodes on level 0 is 3, 
        # on level 1 is 14.5, and on level 2 is 11.
        solution = Solution()
        root = self.create_binary_tree([3, 9, 20, None, None, 15, 7])
        result = solution.averageOfLevels(root)
        expected = [3.00000, 14.50000, 11.00000]
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=5)

    def test_example_2(self):
        # Example 2: Input: root = [3,9,20,15,7]
        # Output: [3.00000,14.50000,11.00000]
        solution = Solution()
        root = self.create_binary_tree([3, 9, 20, 15, 7])
        result = solution.averageOfLevels(root)
        expected = [3.00000, 14.50000, 11.00000]
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=5)

    def test_empty_tree(self):
        # Test with empty tree
        # Output: []
        solution = Solution()
        root = self.create_binary_tree([])
        result = solution.averageOfLevels(root)
        self.assertEqual(result, [])

    def test_single_node(self):
        # Test with single node
        # Input: root = [5]
        # Output: [5.00000]
        solution = Solution()
        root = self.create_binary_tree([5])
        result = solution.averageOfLevels(root)
        expected = [5.00000]
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=5)