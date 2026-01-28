from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases where head is removed
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head:
            # Check if current node has duplicates
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Link prev to the node after duplicates
                prev.next = head.next
            else:
                # No duplicate, move prev forward
                prev = prev.next
            
            # Move to next node
            head = head.next
        
        return dummy.next