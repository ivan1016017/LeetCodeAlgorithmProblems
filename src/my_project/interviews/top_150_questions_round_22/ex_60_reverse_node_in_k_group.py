from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if we have k nodes to reverse
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            # Reverse k nodes
            prev = None
            curr = head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # head is now the last node in reversed group
            # prev is the new head of this group
            # curr is the start of next group
            # Recursively reverse next groups
            head.next = self.reverseKGroup(curr, k)
            return prev
        
        # Less than k nodes remaining, return as is
        return head