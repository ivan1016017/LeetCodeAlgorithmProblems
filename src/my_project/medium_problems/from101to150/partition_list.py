from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_smaller = smaller_cur = ListNode(0)
        dummy_larger = larger_cur = ListNode(0)
        cur = head
        while cur:
            if cur.val < x:
                smaller_cur.next = cur
                smaller_cur = smaller_cur.next
            else:
                larger_cur.next = cur
                larger_cur = larger_cur.next
            cur = cur.next
        larger_cur.next = None
        smaller_cur.next = dummy_larger.next
        return dummy_smaller.next