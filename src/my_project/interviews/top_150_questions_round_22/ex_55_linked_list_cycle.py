from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's Cycle Detection Algorithm (Two Pointers - Slow and Fast)
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using two pointers
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast meet, there's a cycle
            if slow == fast:
                return True
        
        return False