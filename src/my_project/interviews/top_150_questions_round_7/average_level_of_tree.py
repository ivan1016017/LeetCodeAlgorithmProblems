from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()
        q.append(root)
        answer = list()


        while q: 
            qlen = len(q)
            row = 0
            for i in range(qlen):
                root: Optional[TreeNode] = q.popleft()
                row += root.val
                if root.left: q.append(root.left)
                if root.right: q.append(root.right)
            answer.append(row/qlen)

        return answer 

