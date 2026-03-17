import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_105_construct_quad_tree import Solution, Node


class QuadTreeTestCase(unittest.TestCase):
    
    def serialize_tree(self, root: Optional[Node]) -> List[List[int]]:
        """Serialize quad tree to level order format for comparison."""
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append(None)
            else:
                result.append([1 if node.isLeaf else 0, 1 if node.val else 0])
                if not node.isLeaf:
                    queue.append(node.topLeft)
                    queue.append(node.topRight)
                    queue.append(node.bottomLeft)
                    queue.append(node.bottomRight)
        
        return result
    
    def test_example_1(self):
        """Test with 2x2 grid with different values."""
        grid = [[0, 1], [1, 0]]
        solution = Solution()
        result = solution.construct(grid)
        
        # Root should not be a leaf
        self.assertFalse(result.isLeaf)
        
        # All four children should be leaves
        self.assertTrue(result.topLeft.isLeaf)
        self.assertTrue(result.topRight.isLeaf)
        self.assertTrue(result.bottomLeft.isLeaf)
        self.assertTrue(result.bottomRight.isLeaf)
        
        # Check values
        self.assertFalse(result.topLeft.val)  # 0
        self.assertTrue(result.topRight.val)  # 1
        self.assertTrue(result.bottomLeft.val)  # 1
        self.assertFalse(result.bottomRight.val)  # 0
    
    def test_example_2(self):
        """Test with 8x8 grid."""
        grid = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]
        ]
        solution = Solution()
        result = solution.construct(grid)
        
        # Root should not be a leaf
        self.assertFalse(result.isLeaf)
        
        # TopLeft should be a leaf with value 1
        self.assertTrue(result.topLeft.isLeaf)
        self.assertTrue(result.topLeft.val)
        
        # BottomLeft should be a leaf with value 1
        self.assertTrue(result.bottomLeft.isLeaf)
        self.assertTrue(result.bottomLeft.val)
        
        # BottomRight should be a leaf with value 0
        self.assertTrue(result.bottomRight.isLeaf)
        self.assertFalse(result.bottomRight.val)
        
        # TopRight should not be a leaf (has different values)
        self.assertFalse(result.topRight.isLeaf)
    
    def test_all_ones(self):
        """Test with grid of all 1's."""
        grid = [[1, 1], [1, 1]]
        solution = Solution()
        result = solution.construct(grid)
        
        # Should be a single leaf node
        self.assertTrue(result.isLeaf)
        self.assertTrue(result.val)
        self.assertIsNone(result.topLeft)
        self.assertIsNone(result.topRight)
        self.assertIsNone(result.bottomLeft)
        self.assertIsNone(result.bottomRight)
    
    def test_all_zeros(self):
        """Test with grid of all 0's."""
        grid = [[0, 0], [0, 0]]
        solution = Solution()
        result = solution.construct(grid)
        
        # Should be a single leaf node
        self.assertTrue(result.isLeaf)
        self.assertFalse(result.val)
        self.assertIsNone(result.topLeft)
        self.assertIsNone(result.topRight)
        self.assertIsNone(result.bottomLeft)
        self.assertIsNone(result.bottomRight)
    
    def test_single_cell(self):
        """Test with 1x1 grid."""
        grid = [[1]]
        solution = Solution()
        result = solution.construct(grid)
        
        self.assertTrue(result.isLeaf)
        self.assertTrue(result.val)


if __name__ == '__main__':
    unittest.main()