import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
    .ex_104_sorted_list import Solution, ListNode


class SortedListTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def list_to_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        """Helper function to convert array to linked list."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_list(self, head: Optional[ListNode]) -> List[int]:
        """Helper function to convert linked list to array."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def test_example_1(self):
        # Input: head = [4,2,1,3]
        # Output: [1,2,3,4]
        head = self.list_to_linked_list([4, 2, 1, 3])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4])
    
    def test_example_2(self):
        # Input: head = [-1,5,3,4,0]
        # Output: [-1,0,3,4,5]
        head = self.list_to_linked_list([-1, 5, 3, 4, 0])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [-1, 0, 3, 4, 5])
    
    def test_example_3(self):
        # Input: head = []
        # Output: []
        head = self.list_to_linked_list([])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [])
    
    def test_single_node(self):
        # Input: head = [1]
        # Output: [1]
        head = self.list_to_linked_list([1])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [1])
    
    def test_two_nodes(self):
        # Input: head = [2,1]
        # Output: [1,2]
        head = self.list_to_linked_list([2, 1])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 2])
    
    def test_already_sorted(self):
        # Input: head = [1,2,3,4,5]
        # Output: [1,2,3,4,5]
        head = self.list_to_linked_list([1, 2, 3, 4, 5])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        # Input: head = [5,4,3,2,1]
        # Output: [1,2,3,4,5]
        head = self.list_to_linked_list([5, 4, 3, 2, 1])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4, 5])
    
    def test_duplicates(self):
        # Input: head = [3,1,2,3,1]
        # Output: [1,1,2,3,3]
        head = self.list_to_linked_list([3, 1, 2, 3, 1])
        result = self.solution.sortList(head)
        self.assertEqual(self.linked_list_to_list(result), [1, 1, 2, 3, 3])