

if __name__ == '__main__':
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class Solution:
        def maxDepth(self, root: TreeNode) -> int:

            try:
                root.left
                root.right
            except:
                root = None

            if root == None:
                return 0
            else:
                left_depth = self.maxDepth(root.left)
                right_depth = self.maxDepth(root.right)

            if left_depth < right_depth:
                return right_depth + 1
            if left_depth >= right_depth:
                return left_depth + 1


    solution = Solution()