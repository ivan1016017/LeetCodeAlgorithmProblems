from typing import List


if __name__ == '__main__':
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    class Solution:
        def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

            if n == 1:
                try:
                    head.next.val
                except:
                    return ListNode(head.next)
                return head.next

            elif n >1:
                while i <= n:
                    if i == n:
                        try:
                            head.next.val
                        except:
                            return ListNode(head.next)
                        return head.next
