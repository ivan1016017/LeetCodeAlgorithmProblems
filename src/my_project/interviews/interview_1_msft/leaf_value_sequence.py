# Definition for a binary tree node.
from typing import List, Union, Optional
from abc import ABC, abstractmethod
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode],result:List[int]):

            if node is None: 
                return None 
            if node.left is None and node.right is None:
                result.append(node.val)
            else: 
                dfs(node.left,result)
                dfs(node.right,result)


        first_leave_nodes = []
        second_leave_nodes = []

        dfs(root1,first_leave_nodes)
        dfs(root2,second_leave_nodes)

        return first_leave_nodes == second_leave_nodes


        pass