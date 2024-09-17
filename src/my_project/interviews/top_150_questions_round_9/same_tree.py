from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p and q: 
            return p.val == q.val \
                   and self.isSameTree(p.left, q.left) \
                   and self.isSameTree(p.right, q.right)
        else: 
            return p is q 

