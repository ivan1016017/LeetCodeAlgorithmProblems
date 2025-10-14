from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        if not root: 
            return False 
        if not root.left and not root.right and root.val == targetSum: 
            return True 
        else: 
            targetSum = targetSum - root.val 
            return self.hasPathSum(root.left, targetSum) \
                   or self.hasPathSum(root.right, targetSum)