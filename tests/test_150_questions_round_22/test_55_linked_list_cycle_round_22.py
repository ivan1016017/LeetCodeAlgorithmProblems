import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_55_linked_list_cycle import Solution, ListNode

class LinkedListTestCase(unittest.TestCase):

    def create_linked_list_with_cycle(self, values, pos):
        """
        Helper function to create a linked list with a cycle.
        
        :param values: List of node values
        :param pos: Index where tail connects (-1 means no cycle)
        :return: Head of the linked list
        """
        if not values:
            return None
        
        # Create all nodes
        nodes = [ListNode(val) for val in values]
        
        # Link nodes in sequence
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        # Create cycle if pos is valid
        if pos >= 0 and pos < len(nodes):
            nodes[-1].next = nodes[pos]
        
        return nodes[0]

    def test_first_pattern(self):
        # Input: head = [3,2,0,-4], pos = 1
        # Output: true
        solution = Solution()
        head = self.create_linked_list_with_cycle([3, 2, 0, -4], 1)
        output = solution.hasCycle(head)
        target = True
        self.assertEqual(output, target)

    def test_second_pattern(self):
        # Input: head = [1,2], pos = 0
        # Output: true
        solution = Solution()
        head = self.create_linked_list_with_cycle([1, 2], 0)
        output = solution.hasCycle(head)
        target = True
        self.assertEqual(output, target)

    def test_third_pattern(self):
        # Input: head = [1], pos = -1
        # Output: false
        solution = Solution()
        head = self.create_linked_list_with_cycle([1], -1)
        output = solution.hasCycle(head)
        target = False
        self.assertEqual(output, target)