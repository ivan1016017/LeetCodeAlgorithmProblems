from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        try: 
            root.val
        except: 
            return root
        
        root.left, root.right = (self.invertTree(root.right),
                                 self.invertTree(root.left))
        
        return root