import unittest
from src.my_project.interviews.top_150_questions_round_1.\
merge_two_sorted_linked_lists import Solution, ListNode

class MergeTwoSortedLinkedListsTestCase(unittest.TestCase):

    def test_merge_sorted_linked_lists(self):
        solution = Solution()
        sorted_1 = ListNode(1,ListNode(2,ListNode(4)))
        sorted_2 = ListNode(1,ListNode(3,ListNode(4)))
        output = solution.mergeTwoLists(l1=sorted_1,l2=sorted_2)
        self.assertEqual(1,output.val)
        self.assertEqual(1,output.next.val)
        self.assertEqual(2,output.next.next.val)
        self.assertEqual(3,output.next.next.next.val)
        self.assertEqual(4,output.next.next.next.next.val)
        self.assertEqual(4,output.next.next.next.next.next.val)

    def test_l1_none(self):
        solution = Solution()
        sorted_1 = None 
        sorted_2 = ListNode(1)
        output = solution.mergeTwoLists(l1=sorted_1,l2=sorted_2)
        self.assertEqual(1,output.val)

    def test_l2_none(self):
        solution = Solution()
        sorted_1 = ListNode(1)
        sorted_2 = None
        output = solution.mergeTwoLists(l1=sorted_1,l2=sorted_2)
        self.assertEqual(1,output.val)