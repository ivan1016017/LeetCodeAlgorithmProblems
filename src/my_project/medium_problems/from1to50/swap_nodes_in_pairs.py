from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp_list = self.ListNodeToLIst(head)
        temp_list = self.swapPairList(temp_list)
        return self.ListToListNode(temp_list)

    def swapPairList(self, list_numbers: List[int]) -> List[int]:
        temp_list = list()
        len_numbers = len(list_numbers)
        for i in range(0, len_numbers,2):
            if i == len_numbers-1:
                temp_list.append(list_numbers[i])
            else:
                temp_list.append(list_numbers[i+1])
                temp_list.append(list_numbers[i])
        return temp_list

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
sample_listnode = ListNode(1,ListNode(2,ListNode(3, ListNode(4,5))))
print(solution.swapPairs(sample_listnode).next.next.next.next.val)