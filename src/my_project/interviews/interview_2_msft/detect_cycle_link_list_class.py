from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        s = set()
        while head: 
            if head in s: 
                return head 
            s.add(head)
            head = head.next
        
        