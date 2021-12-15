from typing import List, Optional 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if root is None: 
            return []

        def traversal(node, path):
            if node.left is None and node.right is None:
                answer.append("->".join(path))
                
            if node.left:
                path.append(str(node.left.val))
                traversal(node.left, path)
                path.pop()
                
            if node.right:
                path.append(str(node.right.val))
                traversal(node.right, path)
                path.pop()      
    
        answer = []
        path = [str(root.val)]
        traversal(root, path)
        return answer 
    
print("*".join(["1", "2"]))

 
 