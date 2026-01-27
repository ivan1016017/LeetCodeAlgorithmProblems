import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_61_remove_n_node_from_end_of_list import Solution, ListNode

class RemoveNNodeFromEndOfListTestCase(unittest.TestCase):

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
        # Example 1: Input: head = [1,2,3,4,5], n = 2
        # Output: [1,2,3,5]
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        output = solution.removeNthFromEnd(head, 2)
        result = self.linked_list_to_list(output)
        target = [1, 2, 3, 5]
        self.assertEqual(result, target)

    def test_second_pattern(self):
        # Example 2: Input: head = [1], n = 1
        # Output: []
        solution = Solution()
        head = self.create_linked_list([1])
        output = solution.removeNthFromEnd(head, 1)
        result = self.linked_list_to_list(output)
        target = []
        self.assertEqual(result, target)

    def test_third_pattern(self):
        # Example 3: Input: head = [1,2], n = 1
        # Output: [1]
        solution = Solution()
        head = self.create_linked_list([1, 2])
        output = solution.removeNthFromEnd(head, 1)
        result = self.linked_list_to_list(output)
        target = [1]
        self.assertEqual(result, target)