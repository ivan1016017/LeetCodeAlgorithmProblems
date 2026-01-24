from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Approach 1: Using HashMap
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head:
            return None
        
        # Map old nodes to new nodes
        old_to_new = {}
        
        # First pass: create all new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: assign next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]
