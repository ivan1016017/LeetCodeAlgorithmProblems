import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_103_convert_sorted_array_to_binary_tree import Solution, TreeNode


class ConvertSortedArrayToBinaryTreeTestCase(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def is_valid_bst(self, root: Optional[TreeNode], min_val: float = float('-inf'), 
                     max_val: float = float('inf')) -> bool:
        """Helper function to check if tree is a valid BST."""
        if not root:
            return True
        
        if root.val <= min_val or root.val >= max_val:
            return False
        
        return (self.is_valid_bst(root.left, min_val, root.val) and 
                self.is_valid_bst(root.right, root.val, max_val))
    
    def get_height(self, root: Optional[TreeNode]) -> int:
        """Helper function to get height of tree."""
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
    
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        """Helper function to check if tree is height-balanced."""
        if not root:
            return True
        
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self.is_balanced(root.left) and self.is_balanced(root.right)
    
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """Helper function to get inorder traversal of tree."""
        if not root:
            return []
        return (self.inorder_traversal(root.left) + 
                [root.val] + 
                self.inorder_traversal(root.right))
    
    def test_example_1(self):
        """
        Input: nums = [-10,-3,0,5,9]
        Output: [0,-3,9,-10,null,5]
        Explanation: [0,-10,5,null,-3,null,9] is also accepted
        """
        nums = [-10, -3, 0, 5, 9]
        result = self.solution.sortedArrayToBST(nums)
        
        # Verify it's a valid BST
        self.assertTrue(self.is_valid_bst(result))
        
        # Verify it's height-balanced
        self.assertTrue(self.is_balanced(result))
        
        # Verify inorder traversal matches the sorted input
        self.assertEqual(self.inorder_traversal(result), nums)
    
    def test_example_2(self):
        """
        Input: nums = [1,3]
        Output: [3,1]
        Explanation: [1,null,3] and [3,1] are both height-balanced BSTs
        """
        nums = [1, 3]
        result = self.solution.sortedArrayToBST(nums)
        
        # Verify it's a valid BST
        self.assertTrue(self.is_valid_bst(result))
        
        # Verify it's height-balanced
        self.assertTrue(self.is_balanced(result))
        
        # Verify inorder traversal matches the sorted input
        self.assertEqual(self.inorder_traversal(result), nums)
    
    def test_single_element(self):
        """Test with single element array."""
        nums = [1]
        result = self.solution.sortedArrayToBST(nums)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)
    
    def test_empty_array(self):
        """Test with empty array."""
        nums = []
        result = self.solution.sortedArrayToBST(nums)
        
        self.assertIsNone(result)
    
    def test_larger_array(self):
        """Test with larger sorted array."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.solution.sortedArrayToBST(nums)
        
        # Verify it's a valid BST
        self.assertTrue(self.is_valid_bst(result))
        
        # Verify it's height-balanced
        self.assertTrue(self.is_balanced(result))
        
        # Verify inorder traversal matches the sorted input
        self.assertEqual(self.inorder_traversal(result), nums)
    
    def test_negative_numbers(self):
        """Test with all negative numbers."""
        nums = [-10, -8, -6, -4, -2]
        result = self.solution.sortedArrayToBST(nums)
        
        # Verify it's a valid BST
        self.assertTrue(self.is_valid_bst(result))
        
        # Verify it's height-balanced
        self.assertTrue(self.is_balanced(result))
        
        # Verify inorder traversal matches the sorted input
        self.assertEqual(self.inorder_traversal(result), nums)
    
    def test_two_elements(self):
        """Test with two elements."""
        nums = [0, 1]
        result = self.solution.sortedArrayToBST(nums)
        
        # Verify it's a valid BST
        self.assertTrue(self.is_valid_bst(result))
        
        # Verify it's height-balanced
        self.assertTrue(self.is_balanced(result))
        
        # Verify inorder traversal matches the sorted input
        self.assertEqual(self.inorder_traversal(result), nums)