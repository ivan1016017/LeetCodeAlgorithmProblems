from typing import List, Optional 
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        q = deque([(root, 0)])
        while q:
            length = len(q)
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            for _ in range(length):
                node, x = q.popleft()
                if node.left:
                    q.append((node.left, 2 * x))
                if node.right:
                    q.append((node.right, 2 * x + 1))
                    
        return max_width