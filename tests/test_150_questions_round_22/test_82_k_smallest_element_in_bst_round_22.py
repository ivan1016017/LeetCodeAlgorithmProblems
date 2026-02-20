import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_82_k_smallest_element_in_bst import Solution, TreeNode

class BinaryTreeLevelOrderTraversalTestCase(unittest.TestCase):

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
        # Example 1: Input: root = [3,1,4,null,2], k = 1
        # Output: 1
        solution = Solution()
        root = self.create_binary_tree([3, 1, 4, None, 2])
        result = solution.kthSmallest(root, 1)
        self.assertEqual(result, 1)

    def test_example_2(self):
        # Example 2: Input: root = [5,3,6,2,4,null,null,1], k = 3
        # Output: 3
        solution = Solution()
        root = self.create_binary_tree([5, 3, 6, 2, 4, None, None, 1])
        result = solution.kthSmallest(root, 3)
        self.assertEqual(result, 3)