from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a flag
        flag = False
        temp = ListNode(0)
        current = temp
        # check the initial conditions of l1 and l2
        is_l1_numeric = isinstance(l1.val, int) or isinstance(l1.val, float)
        is_l2_numeric = isinstance(l2.val, int) or isinstance(l2.val, float)
        if is_l1_numeric and not is_l2_numeric:
            temp = l1
            flag = True
        elif not is_l1_numeric and is_l2_numeric:
            temp = l2
            flag = True
        elif not is_l1_numeric and not is_l2_numeric:
            temp = ListNode("")
            flag = True
        else:
            is_l1_none = False
            is_l2_none = False
            while not flag:
                # compare values
                if l1.val < l2.val:
                    # insert the lower value in ListNode.
                    current.val = l1.val
                    print(current.val)
                    l1 = l1.next
                    current.next = ListNode(0)
                    current = current.next
                    is_l1_none = l1 is None
                    if is_l1_none:
                        current.val = l2.val
                        current.next = l2.next
                        print(current.val, current.next.val)
                        flag = True
                    print(is_l1_none)
                    # assign the next value of the lowest value to temp_l1 or temp_l2
                else:
                    current.val = l2.val
                    print(current.val)
                    l2 = l2.next
                    current.next = ListNode(0)
                    current = current.next
                    is_l2_none = l2 is None
                    if is_l2_none:
                        current.val = l1.val
                        current.next = l1.next
                        flag = True

        return temp

# sample_linked_one = ListNode(1, ListNode(2,ListNode(3)))
# sample_linked_two = ListNode(3, ListNode(4,ListNode(5)))
sample_linked_one = ListNode("")
sample_linked_two = ListNode("")

solution = Solution()
a = solution.mergeTwoLists(sample_linked_one, sample_linked_two)
# print(a.val, a.next.val, a.next.next.val, a.next.next.next.val, a.next.next.next.next.val,
#       a.next.next.next.next.next.val)
# print(a.val, a.next.val, a.next.next.val)
print(a.val)