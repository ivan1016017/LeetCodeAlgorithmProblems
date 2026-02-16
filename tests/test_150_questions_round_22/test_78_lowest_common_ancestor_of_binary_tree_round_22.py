import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_78_lowest_common_ancestor_of_binary_tree import Solution, TreeNode


class LowestCommonAncestorBinaryTreeTestCase(unittest.TestCase):

    def build_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """Build a binary tree from level-order array representation."""
        if not values or values[0] is None:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def find_node(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Find a node with given value in the tree."""
        if not root:
            return None
        if root.val == val:
            return root
        left = self.find_node(root.left, val)
        if left:
            return left
        return self.find_node(root.right, val)

    def test_example_1(self):
        """Test case: LCA of nodes 5 and 1 is 3."""
        solution = Solution()
        tree = self.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = self.find_node(tree, 5)
        q = self.find_node(tree, 1)
        output = solution.lowestCommonAncestor(root=tree, p=p, q=q)
        self.assertEqual(3, output.val)

    def test_example_2(self):
        """Test case: LCA of nodes 5 and 4 is 5 (node can be ancestor of itself)."""
        solution = Solution()
        tree = self.build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = self.find_node(tree, 5)
        q = self.find_node(tree, 4)
        output = solution.lowestCommonAncestor(root=tree, p=p, q=q)
        self.assertEqual(5, output.val)

    def test_example_3(self):
        """Test case: LCA of nodes 1 and 2 is 1."""
        solution = Solution()
        tree = self.build_tree([1, 2])
        p = self.find_node(tree, 1)
        q = self.find_node(tree, 2)
        output = solution.lowestCommonAncestor(root=tree, p=p, q=q)
        self.assertEqual(1, output.val)