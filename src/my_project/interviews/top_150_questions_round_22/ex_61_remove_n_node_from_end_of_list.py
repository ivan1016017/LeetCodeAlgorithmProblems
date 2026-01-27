from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node to handle edge cases (e.g., removing the head)
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Skip the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next