from typing import List



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # initialize flag
        flag = True

        # from LinkedList to List
        head_list = self.fromListNodeToList(head)
        len_head_list = len(head_list)
        print(head_list)
        # check palindrome
        for i in range(len_head_list):
            if head_list[i] != head_list[len_head_list-1-i]:
                print("flag")
                flag = False
                break
        return flag


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


solution = Solution()

print(solution.isPalindrome(ListNode(1,ListNode(2,ListNode(2,1)))))
