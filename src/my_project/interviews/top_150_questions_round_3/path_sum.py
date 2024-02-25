from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: 
            return False
        elif not root.left and not root.right and root.val == targetSum:
            return True 
        else: 
            temp_target = targetSum - root.val 
            return self.hasPathSum(root=root.left, targetSum=temp_target) or \
                self.hasPathSum(root=root.right, targetSum=temp_target)