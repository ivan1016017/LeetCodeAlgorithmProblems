import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_56_add_two_numbers import Solution, ListNode


class AddTwoLinkedListsTestCase(unittest.TestCase):

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
        # Input: l1 = [2,4,3], l2 = [5,6,4]
        # Output: [7,0,8]
        # Explanation: 342 + 465 = 807
        solution = Solution()
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        output = solution.addTwoNumbers(l1, l2)
        result = self.linked_list_to_list(output)
        target = [7, 0, 8]
        self.assertEqual(result, target)

    def test_second_pattern(self):
        # Input: l1 = [0], l2 = [0]
        # Output: [0]
        solution = Solution()
        l1 = self.create_linked_list([0])
        l2 = self.create_linked_list([0])
        output = solution.addTwoNumbers(l1, l2)
        result = self.linked_list_to_list(output)
        target = [0]
        self.assertEqual(result, target)

    def test_third_pattern(self):
        # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        # Output: [8,9,9,9,0,0,0,1]
        solution = Solution()
        l1 = self.create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.create_linked_list([9, 9, 9, 9])
        output = solution.addTwoNumbers(l1, l2)
        result = self.linked_list_to_list(output)
        target = [8, 9, 9, 9, 0, 0, 0, 1]
        self.assertEqual(result, target)