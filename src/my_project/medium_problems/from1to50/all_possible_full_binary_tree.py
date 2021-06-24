from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepCopy(self, node):
        if not node:
            return None
        copy_node = TreeNode(node.val)
        copy_node.left = self.deepCopy(node.left)
        copy_node.right = self.deepCopy(node.right)
        return copy_node

    def allPossibleFBT(self, n: int) -> List[TreeNode]:

        dp = [[] for i in range(n + 1)]
        dp[1] = [TreeNode(0)]

        for i in range(3, n + 1):
            for l in range(i - 1):
                r = i - 1 - l
                for node_l in dp[l]:
                    for node_r in dp[r]:
                        dp[i].append(TreeNode(0, self.deepCopy(node_l), self.deepCopy(node_r)))

        return dp


solution = Solution()

for i in solution.allPossibleFBT(5):
    print(i)