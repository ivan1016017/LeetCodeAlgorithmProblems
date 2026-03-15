from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Choose middle element as root to ensure height-balanced tree
            mid = (left + right) // 2
            
            # Create root node with middle element
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            
            return root
        
        return buildBST(0, len(nums) - 1)
        