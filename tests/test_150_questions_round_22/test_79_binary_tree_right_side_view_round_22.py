import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_79_binary_tree_right_side_view import Solution, TreeNode

class BinaryTreeRightSideViewTestCase(unittest.TestCase):

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
        # Example 1: Input: root = [1,2,3,null,5,null,4]
        # Output: [1,3,4]
        solution = Solution()
        root = self.create_binary_tree([1, 2, 3, None, 5, None, 4])
        result = solution.rightSideView(root)
        self.assertEqual(result, [1, 3, 4])

    def test_example_2(self):
        # Example 2: Input: root = [1,2,3,4,null,null,null,5]
        # Output: [1,3,4,5]
        solution = Solution()
        root = self.create_binary_tree([1, 2, 3, 4, None, None, None, 5])
        result = solution.rightSideView(root)
        self.assertEqual(result, [1, 3, 4, 5])

    def test_example_3(self):
        # Example 3: Input: root = [1,null,3]
        # Output: [1,3]
        solution = Solution()
        root = self.create_binary_tree([1, None, 3])
        result = solution.rightSideView(root)
        self.assertEqual(result, [1, 3])

    def test_example_4(self):
        # Example 4: Input: root = []
        # Output: []
        solution = Solution()
        root = self.create_binary_tree([])
        result = solution.rightSideView(root)
        self.assertEqual(result, [])