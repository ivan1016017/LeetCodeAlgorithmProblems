from typing import List


if __name__ == '__main__':
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    class Solution:
        def hasCycle(self, head: ListNode) -> bool:
            temp = head
            temp_set = set()
            while (temp.next):
                if temp.val in temp_set and temp.next is None:
                    return True
                temp_set.add(temp.val)
                temp = temp.next

            return False




    solution = Solution()
    # print(solution.ListNodeToList(ListNode(1,ListNode(2,ListNode(1)))))
    # print(solution.ListNodeToList(ListNode(1,ListNode(2))))







