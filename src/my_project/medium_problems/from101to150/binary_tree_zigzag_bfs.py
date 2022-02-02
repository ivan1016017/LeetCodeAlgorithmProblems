from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in range(len(stack)):
                
                node=stack.pop(0)
                temp+=[node.val]
                print(temp)
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res
        
solution = Solution()

print(solution.zigzagLevelOrder(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))