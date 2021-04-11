
if __name__ == '__main__':
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    class Solution:
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

    print("Hello")