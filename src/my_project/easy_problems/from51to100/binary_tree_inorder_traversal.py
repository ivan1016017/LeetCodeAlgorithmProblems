from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.temp = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.listTraversal(root)


        return self.temp

    def listTraversal(self, root: TreeNode):
        if root is not None:
            self.inorderTraversal(root.left)
            self.temp.append(root.val)
            self.inorderTraversal(root.right)

solution = Solution()

print(solution.inorderTraversal(TreeNode(1,TreeNode(2))))