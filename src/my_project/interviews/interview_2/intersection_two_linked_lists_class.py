from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_nodes = dict()
        pointer_a: ListNode = headA
        pointer_b: ListNode = headB

        while pointer_a:
            list_nodes[pointer_a] = pointer_a
            pointer_a = pointer_a.next 
        
        while pointer_b:
            if pointer_b in list_nodes:
                return pointer_b
            pointer_b = pointer_b.next