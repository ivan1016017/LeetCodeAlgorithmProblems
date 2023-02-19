from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def closestValue(self, root, target):
        if not root:
            return 0
        self.res = root.val
        self.findClosest(root, target)
        return self.res
        
    def findClosest(self, root, target):
        if root:
            if abs(root.val-target) == 0:
                self.res = root.val
                return  # backtracking 
            if abs(root.val-target) < abs(self.res - target):
                self.res = root.val
            self.findClosest(root.left, target)
            self.findClosest(root.right, target)

class SolutionTwo():
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        trav = root
        minimum = trav.val
        while trav:
            if abs(trav.val - target) < abs(minimum - target):
                minimum = trav.val
            if trav.val == target:
                return trav.val
            elif trav.val < target:
                trav = trav.right
            else:
                trav = trav.left
        return minimum
                

solution_two = Solution()
root = TreeNode(4,TreeNode(2,TreeNode(100),TreeNode(300)),TreeNode(3))
root_fix = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(5))
print(solution_two.closestValue(root,3))