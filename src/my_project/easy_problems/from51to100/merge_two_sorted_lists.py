# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        solution = ListNode()
        temp = solution

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1 is not None or l2 is not None:

            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    temp.val = l1.val
                    l1 = l1.next
                    if l1 is None:
                        temp.next = l2
                        return solution
                    temp.next = ListNode()
                    temp = temp.next

                    continue
                if l1.val >= l2.val:
                    temp.val = l2.val
                    l2 = l2.next
                    if l2 is None:
                        temp.next = l1
                        return solution
                    temp.next = ListNode()
                    temp = temp.next

                    continue


solution = Solution()

a = ListNode(1,ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(3, ListNode(4)))
print(solution.mergeTwoLists(a,b).val)
print(solution.mergeTwoLists(a,b).next.val)
print(solution.mergeTwoLists(a,b).next.next.val)
print(solution.mergeTwoLists(a,b).next.next.next.val)
print(solution.mergeTwoLists(a,b).next.next.next.next.val)
print(solution.mergeTwoLists(a,b).next.next.next.next.next.val)
print(solution.mergeTwoLists(a,b).next.next.next.next.next.next)

