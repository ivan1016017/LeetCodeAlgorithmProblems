from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create a dummy node to handle edge cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 1: Move to the node before the left position
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 2: Reverse the sublist from left to right
        # prev points to the node before left position
        # current points to the left position
        current = prev.next
        
        # Reverse nodes from left to right
        for _ in range(right - left):
            # Save the next node to move
            next_node = current.next
            # Point current.next to the node after next_node
            current.next = next_node.next
            # Insert next_node right after prev
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next