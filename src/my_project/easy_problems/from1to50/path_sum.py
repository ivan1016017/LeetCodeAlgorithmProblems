


if __name__ == '__main__':
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right



    solution = Solution()
    print(solution.hasPathSum(TreeNode(5,4,0), 9))