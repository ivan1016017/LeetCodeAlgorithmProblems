from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque, defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # Divide and conquer approach
        return self._merge_lists(lists, 0, len(lists) - 1)
    
    def _merge_lists(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        
        if left < right:
            mid = (left + right) // 2
            l1 = self._merge_lists(lists, left, mid)
            l2 = self._merge_lists(lists, mid + 1, right)
            return self._merge_two_lists(l1, l2)
        
        return None
    
    def _merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach remaining nodes
        if l1 is not None:
            current.next = l1
        if l2 is not None:
            current.next = l2
        
        return dummy.next
