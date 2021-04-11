

if __name__ == '__main__':
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class Solution:
        def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False
            try:
                p.val
                q.val
            except:
                print(p, q)
                return p == q
            return ((p.val == q.val) and  self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))






    # sample_tree = TreeNode(1,2)
    # print(sample_tree.val, sample_tree.left, sample_tree.right)
    solution = Solution()
    print(solution.isSameTree(TreeNode(1,2,3), TreeNode(1,2,TreeNode(None, None,15))))