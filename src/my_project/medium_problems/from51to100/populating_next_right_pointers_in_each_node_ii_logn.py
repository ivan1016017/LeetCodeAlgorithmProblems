from typing import List 
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        dummy = Node(0)
        curr = root
        while curr:
            dummy.next = None
            tmp = dummy
            while curr:
                if curr.left:
                    tmp.next = curr.left
                    tmp = tmp.next
                if curr.right:
                    tmp.next = curr.right
                    tmp = tmp.next
                curr = curr.next
            curr = dummy.next

        return root