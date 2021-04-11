from typing import List



if __name__ == '__main__':
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:

            # initialize the flag
            # loop while flag is true
            temp_list = self.fromListNodeToList(head)
            temp_list = self.removeDuplicatesList(temp_list)
            temp_list_node = self.from_list_listNode(temp_list)

            return temp_list_node

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


        def removeDuplicatesList(self, list_numbers):
            temp = []
            len_numbers = len(list_numbers)
            if len_numbers == 0:
                return []
            else:
                temp.append(list_numbers[0])
                if len_numbers >= 2:
                    for i in range(1,len_numbers):
                        if list_numbers[i] not in temp:
                            temp.append(list_numbers[i])

            return temp

        def from_list_listNode(self, list_numbers: List[int]) -> List[ListNode]:
            # define the scenario where the list is None
            # define the scenario where the list is empty
            if list_numbers is None or list_numbers == []:
                return []
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

    first_sample = ListNode(1,ListNode(2,3))
    second_sample = ListNode(1,ListNode(2))
    third_sample = ListNode(1,ListNode(1,ListNode(2,ListNode(2,3))))
    solution = Solution()
    print(solution.fromListNodeToList(first_sample))
    print(solution.fromListNodeToList(second_sample))
    a = solution.from_list_listNode([1,2,3])
    b = solution.deleteDuplicates(ListNode())
    print(b)



