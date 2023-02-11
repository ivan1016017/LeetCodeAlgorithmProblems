from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        temp_treenode = TreeNode()
        if not nums:
            return None
        middle_index = len(nums)//2

        temp_treenode.val = nums[middle_index]

        temp_treenode.left = self.sortedArrayToBST(nums[:middle_index])
        temp_treenode.right = self.sortedArrayToBST(nums[middle_index+1:])

        return temp_treenode