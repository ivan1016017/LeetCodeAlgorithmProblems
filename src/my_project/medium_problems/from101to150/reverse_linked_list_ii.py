from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        current = head
        m = left
        n = right
        i = 1
        while i < m and current:
            prev = current
            current = current.next
            i += 1
        start = current
        end = None
        while i <= n and current:
            next = current.next
            current.next = end
            end = current
            current = next
            i += 1

        start.next = current

        if not prev:
            head = end
        else:
            prev.next = end

        return head