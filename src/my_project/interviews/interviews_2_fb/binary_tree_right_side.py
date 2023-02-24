from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.temp = list()

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
    
        q = [root]

        nxt = []

        level = []

        res = []


        while q!=[]:
            for root in q:
                level.append(root.val)

                if root.left:
                    nxt.append(root.left)

                if root.right:
                    nxt.append(root.right)

            res.append(level[-1])

            level = []

            q= nxt
            nxt =[]

        return res