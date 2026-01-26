import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_60_reverse_node_in_k_group import Solution, ListNode

class ReverseNodeInKGroupTestCase(unittest.TestCase):

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
        # Example 1: Input: head = [1,2,3,4,5], k = 2
        # Output: [2,1,4,3,5]
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        output = solution.reverseKGroup(head, 2)
        result = self.linked_list_to_list(output)
        target = [2, 1, 4, 3, 5]
        self.assertEqual(result, target)

    def test_second_pattern(self):
        # Example 2: Input: head = [1,2,3,4,5], k = 3
        # Output: [3,2,1,4,5]
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        output = solution.reverseKGroup(head, 3)
        result = self.linked_list_to_list(output)
        target = [3, 2, 1, 4, 5]
        self.assertEqual(result, target)