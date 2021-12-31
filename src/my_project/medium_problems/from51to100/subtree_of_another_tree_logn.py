from typing import List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def checkSubtree(self,root,subRoot): # function to check if tree and  subtree are equal

        if root is None and subRoot is None:
            return True 
        elif root is None or subRoot is None:
            return False 
        else: 
            if root.val == subRoot.val:
                v1 = self.checkSubtree(root.left, subRoot.left)
                v2 = self.checkSubtree(root.right, subRoot.right)
                
                return v1 and v2 
            return False 
        
    def isSubtree(self, root, subRoot) -> bool: # function to traverse the whole tree
        if root is None:
            return False 
        else: 
            v1 = False 
            if root.val ==subRoot.val:
                v1 = self.checkSubtree(root,subRoot)
                
            v2 = self.isSubtree(root.left, subRoot)
            v3 = self.isSubtree(root.right, subRoot)
            
        return v1 or v2 or v3
                