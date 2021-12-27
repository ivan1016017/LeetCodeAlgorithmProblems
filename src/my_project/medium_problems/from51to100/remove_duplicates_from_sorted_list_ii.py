from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if (head == None):
            return None 
        if (head.next == None):
            return head 
        if (head.val == head.next.val):
            temp = self.deleteDuplicates(head.next)
            while(temp!=None):
                if(temp.val!=head.val):
                    break 
                temp=temp.next
            return temp 
        
        else: 
            head.next = self.deleteDuplicates(head.next)
            return head
                
                
        
        
     