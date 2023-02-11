from typing import List, Union, Mapping, Collection, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.res = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left) + abs(right)
            return root.val + left + right - 1
        dfs(root)
        return self.res


solution = Solution()

print(solution.distributeCoins(TreeNode(0,TreeNode(3),TreeNode(0))))