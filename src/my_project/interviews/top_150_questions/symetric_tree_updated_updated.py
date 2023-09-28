from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    __name_of_instance = 'SolutionOne'

    def __init__(self) -> None:
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instance = self 

    @staticmethod
    def get_instance() -> None: 
        print(Solution.__name_of_instance)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, subtree1:TreeNode, subtree2: TreeNode) ->bool:

        if subtree1 is None and subtree2 is None:
            return True

        if subtree1 is not None and subtree2 is not None:
            try:
                subtree1.val
                subtree2.val
            except:
                return subtree1 == subtree2
            if subtree1.val == subtree2.val:
                return self.isMirror(subtree1.left, subtree2.right) and self.isMirror(subtree1.right, subtree2.left)

        return False
    

class SolutionTwo: 

    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)
        
    def dfs(self, l, r):
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r
        
    def isSymmetric(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r or (l.val != r.val):
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True