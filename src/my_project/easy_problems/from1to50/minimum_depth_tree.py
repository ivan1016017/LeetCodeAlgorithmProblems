
if __name__ == '__main__':
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    class Solution:
        def minDepth(self, root: TreeNode) -> int:

            if root is None:
                return 0

            try:
                root.left
            except:
                try:
                    root.right
                except:
                    return 1
                return self.minDepth(root.right)
            try:
                root.right
            except:
                try:
                    root.left
                except:
                    return 1
                return self.minDepth(root.left)


            if root.left is None and root.right is None:
                return 1

            if root.left is None and root.right is not None:
                return self.minDepth(root.right) +1

            if root.left is not None and root.right is None:
                return self.minDepth(root.left) +1

            return min(self.minDepth(root.left), self.minDepth(root.right))+1


    solution = Solution()
    print(solution.minDepth(TreeNode(3,9,TreeNode(20,15,7))))