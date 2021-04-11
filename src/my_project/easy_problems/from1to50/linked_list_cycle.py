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


    sample = ListNode(1)
    second_sample = ListNode(1)
    second_sample.next = ListNode(2)
    second_sample.next.next = ListNode(1)
    second_sample.next.next.next = ListNode(4)
    # second_sample.next.next.next.next = ListNode(1)

    print(solution.hasCycle(sample))
    print(solution.hasCycle(second_sample))
    # sample.next = ListNode(2)
    # sample.next.next = ListNode(1)
    # print(solution.ListNodeToList(sample))
    # sample_second = ListNode(1)
    # print(solution.hasCycle(sample))
    # print(solution.hasCycle(sample_second))

    # print(sample.val, sample.next.val, sample.next.next.val)
    set_new = {1,2,3}
    print(type(set_new))
    set_new.add(5)
    print(set_new)
    print(1 in set_new)

    list1 = [1,2,3]
    list2 = [1,2,3]
    print(list1 is list2)





