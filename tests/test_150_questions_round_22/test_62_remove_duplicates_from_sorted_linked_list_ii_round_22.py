import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_62_remove_duplicates_from_sorted_linked_list_ii import Solution, ListNode

class RemoveDuplicatesFromSortedLinkedListsIITestCase(unittest.TestCase):

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
        # Example 1: Input: head = [1,2,3,3,4,4,5]
        # Output: [1,2,5]
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 3, 4, 4, 5])
        output = solution.deleteDuplicates(head)
        result = self.linked_list_to_list(output)
        target = [1, 2, 5]
        self.assertEqual(result, target)

    def test_second_pattern(self):
        # Example 2: Input: head = [1,1,1,2,3]
        # Output: [2,3]
        solution = Solution()
        head = self.create_linked_list([1, 1, 1, 2, 3])
        output = solution.deleteDuplicates(head)
        result = self.linked_list_to_list(output)
        target = [2, 3]
        self.assertEqual(result, target)