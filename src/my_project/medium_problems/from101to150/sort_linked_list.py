from typing import List, Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        myList=[]
        while head:
            myList.append(head.val)
            head=head.next
        myList.sort()
        newHead=point=ListNode(0)
        for i in range(len(myList)):
            point.next=ListNode(myList[i])
            point=point.next
        return newHead.next
        