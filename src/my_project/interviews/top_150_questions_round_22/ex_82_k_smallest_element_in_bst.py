from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Collect all values in sorted order using in-order traversal
        values = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return values[k - 1]