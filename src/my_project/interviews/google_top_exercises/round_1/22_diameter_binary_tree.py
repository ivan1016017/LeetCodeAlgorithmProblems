class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0

        def depth(node):
            """
            Returns the height (in edges) of the subtree rooted at node.
            Updates self.diameter with the longest path through this node.
            """
            if not node:
                return -1

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Path through this node uses both subtrees: edges on each side
            self.diameter = max(self.diameter, left_depth + right_depth + 2)

            # Only one branch can be extended toward the parent
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diameter