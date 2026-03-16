from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort a linked list using merge sort algorithm.
        Time: O(n log n), Space: O(log n) for recursion stack
        """
        if not head or not head.next:
            return head
        
        # Find the middle of the list
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None  # Split the list
        
        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head: ListNode) -> ListNode:
        """Find the middle node using slow and fast pointers."""
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists."""
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next