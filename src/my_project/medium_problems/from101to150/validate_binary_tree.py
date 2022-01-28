from typing import List, Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive in order traversal:
        for a node check to see if:
            min value < node.val < max value     (min, max)
            recurse left -> bound max to node.val since anything on left should be less
            recurse right -> bound min to node.val since anything on right should be greater

        
        """
        
        
        def helper(node, minv=float('-inf'), maxv=float('inf')):
            if node == None:
                return True
            
            # minv < val < maxv
            if not (node.val > minv and node.val < maxv ):
                return False
            
            # branch and bound left child -> bound max
            b1 = helper(node.left, minv, node.val)
            
            # branch and bound right child -> bound min
            b2 = helper(node.right, node.val, maxv)
            
            return b1 and b2
            
            
            
        return helper(root)