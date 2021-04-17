from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        listnode_to_list = self.ListNodeToLIst(head)
        temp_list =list()
        for i in range(len(listnode_to_list)):
            if i != (len(listnode_to_list) - n):
                temp_list.append(listnode_to_list[i])
        return self.ListToListNode(temp_list)
    def ListNodeToLIst(self, head: ListNode) -> List:
        temp_list = list()
        temp_listNode = None


        try:
            head.val
        except:
            return []

        # add first element to list
        temp_list.append(head.val)

        # fill the list
        while head.next:
            temp_listNode = head.next
            head = temp_listNode

            if head:
                try:
                    head.val
                except:
                    temp_list.append(head)
                    break
                temp_list.append(head.val)
            else:
                break
        return temp_list


    def ListToListNode(self, list_numbers: List) -> ListNode:
        # initialize listNode
        result = ListNode(0)

        if list_numbers == []:
            return None
        # loop through the list
        result.val = list_numbers[0]
        temp = result
        for i in range(1,len(list_numbers)):
            temp.next = ListNode(list_numbers[i])
            temp = temp.next
        return result





solution = Solution()

# print(solution.ListNodeToLIst(ListNode(1,ListNode(2,3))))
# print(ListNode(1,3).val)
# print("*************")
# print(solution.ListNodeToLIst(solution.ListToListNode([])))
# a = ListNode(0)
# a.next = ListNode(1,2)
# print(a.next.next)
sample_listNode = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print(solution.removeNthFromEnd(sample_listNode,2).next.next.next.val)
