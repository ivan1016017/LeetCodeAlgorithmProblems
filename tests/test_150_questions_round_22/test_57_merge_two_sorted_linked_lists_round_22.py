import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_57_merge_two_sorted_linked_lists import Solution, ListNode

class MergeTwoLinkedListsTestCase(unittest.TestCase):

    def create_linked_list(self, values):
        """
        Helper function to create a linked list from a list of values.
        
        :param values: List of node values
        :return: Head of the linked list
        """
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head

    def linked_list_to_list(self, head):
        """
        Helper function to convert linked list to Python list.
        
        :param head: Head of the linked list
        :return: List of values
        """
        result = []
        current = head
        
        while current:
            result.append(current.val)
            current = current.next
        
        return result

    def test_first_pattern(self):
        # Input: list1 = [1,2,4], list2 = [1,3,4]
        # Output: [1,1,2,3,4,4]
        solution = Solution()
        l1 = self.create_linked_list([1, 2, 4])
        l2 = self.create_linked_list([1, 3, 4])
        output = solution.mergeTwoLists(l1, l2)
        result = self.linked_list_to_list(output)
        target = [1, 1, 2, 3, 4, 4]
        self.assertEqual(result, target)

    def test_second_pattern(self):
        # Input: list1 = [], list2 = []
        # Output: []
        solution = Solution()
        l1 = self.create_linked_list([])
        l2 = self.create_linked_list([])
        output = solution.mergeTwoLists(l1, l2)
        result = self.linked_list_to_list(output)
        target = []
        self.assertEqual(result, target)

    def test_third_pattern(self):
        # Input: list1 = [], list2 = [0]
        # Output: [0]
        solution = Solution()
        l1 = self.create_linked_list([])
        l2 = self.create_linked_list([0])
        output = solution.mergeTwoLists(l1, l2)
        result = self.linked_list_to_list(output)
        target = [0]
        self.assertEqual(result, target)