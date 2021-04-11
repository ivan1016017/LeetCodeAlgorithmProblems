
if __name__ == '__main__':
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


    class Solution:


        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            def __init__(self):
                self.head = None

            prev = None
            temp_carry = 0
            temp = None

            while (l1 is not None or l2 is not None):

                f_value = 0 if l1 is None else l1.val
                s_value = 0 if l2 is None else l2.val

                sum = temp_carry + f_value + s_value

                temp_carry = 1 if sum >= 10 else 0
                sum = sum if sum < 10 else sum % 10

                temp = ListNode(sum)
                if self.head is None:
                    self.head = temp
                else:
                    prev.next = temp
                prev = temp

                if l1 is not None:
                    l1 = l1.next
                if l2 is not None:
                    l2 = l2.next


            if temp_carry > 0:
                temp.next = ListNode(temp_carry)

            return self.head

    l1 = ListNode(7 ,ListNode(5 ,ListNode(9, ListNode(4, ListNode(6)))))
    l2 = ListNode(8, ListNode(4))

    # print(l1.next.next.next.next.val)
    res = Solution()
    #
    print(res.addTwoNumbers(l1 ,l2).next.next.val)
    # print(res.addTwoNumbers(l1 ,l2).val)


