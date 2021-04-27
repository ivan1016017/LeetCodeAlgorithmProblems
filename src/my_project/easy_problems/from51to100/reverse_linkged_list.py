from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp_list = self.fromListNodeToList(head)
        print(temp_list)
        temp_list.reverse()
        temp_list_node = self.from_list_listNode(temp_list)
        return temp_list_node


    def from_list_listNode(self, list_numbers: List[int]) -> List[ListNode]:
        # define the scenario where the list is None
        # define the scenario where the list is empty
        if list_numbers is None or list_numbers == []:
            return ListNode("")
        # the list is not empty
        # loop through the list
        temp = ListNode(list_numbers[0])
        current = temp
        for i in range(len(list_numbers) - 1):
            # insert list_numbers entry to the ListNode.val
            current.next = ListNode(list_numbers[i + 1])
            # set the next
            current = current.next
        return temp

    def fromListNodeToList(self, list_node: ListNode) -> List:
        temp = list()
        try:
            list_node.val
        except:
            return []
        if list_node.val == "" or list_node.val == None:
            return []
        else:
            while list_node:
                try:
                    temp.append(list_node.val)
                except:
                    temp.append(list_node)
                    break
                list_node = list_node.next
        return temp