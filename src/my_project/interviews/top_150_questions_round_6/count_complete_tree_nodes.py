from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root: 
            return 0
        else: 
            return self.countNodes(root.left) \
                   + self.countNodes(root.right) \
                   + 1