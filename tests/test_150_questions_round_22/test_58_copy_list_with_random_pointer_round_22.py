import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_58_copy_list_with_random_pointer import Solution, Node

class CopyListWithRandomPointerTestCase(unittest.TestCase):

    def create_linked_list_with_random(self, values):
        """
        Helper function to create a linked list with random pointers.
        
        :param values: List of [val, random_index] pairs
        :return: Head of the linked list
        """
        if not values:
            return None
        
        # Create all nodes first
        nodes = []
        for val, _ in values:
            nodes.append(Node(val))
        
        # Connect next pointers and random pointers
        for i in range(len(nodes)):
            if i < len(nodes) - 1:
                nodes[i].next = nodes[i + 1]
            
            random_index = values[i][1]
            if random_index is not None:
                nodes[i].random = nodes[random_index]
        
        return nodes[0]

    def linked_list_to_list(self, head):
        """
        Helper function to convert linked list with random pointers to list format.
        
        :param head: Head of the linked list
        :return: List of [val, random_index] pairs
        """
        if not head:
            return []
        
        # Create a map of nodes to their indices
        node_to_index = {}
        curr = head
        index = 0
        while curr:
            node_to_index[curr] = index
            curr = curr.next
            index += 1
        
        # Build the result
        result = []
        curr = head
        while curr:
            random_index = node_to_index.get(curr.random) if curr.random else None
            result.append([curr.val, random_index])
            curr = curr.next
        
        return result

    def test_example_1(self):
        # Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        # Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
        solution = Solution()
        head = self.create_linked_list_with_random([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        copied_head = solution.copyRandomList(head)
        result = self.linked_list_to_list(copied_head)
        target = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        self.assertEqual(result, target)
        
        # Verify deep copy - nodes should be different objects
        self.assertIsNot(head, copied_head)

    def test_example_2(self):
        # Input: head = [[1,1],[2,1]]
        # Output: [[1,1],[2,1]]
        solution = Solution()
        head = self.create_linked_list_with_random([[1, 1], [2, 1]])
        copied_head = solution.copyRandomList(head)
        result = self.linked_list_to_list(copied_head)
        target = [[1, 1], [2, 1]]
        self.assertEqual(result, target)
        
        # Verify deep copy
        self.assertIsNot(head, copied_head)

    def test_example_3(self):
        # Input: head = [[3,null],[3,0],[3,null]]
        # Output: [[3,null],[3,0],[3,null]]
        solution = Solution()
        head = self.create_linked_list_with_random([[3, None], [3, 0], [3, None]])
        copied_head = solution.copyRandomList(head)
        result = self.linked_list_to_list(copied_head)
        target = [[3, None], [3, 0], [3, None]]
        self.assertEqual(result, target)
        
        # Verify deep copy
        self.assertIsNot(head, copied_head)

    def test_empty_list(self):
        # Input: head = []
        # Output: []
        solution = Solution()
        head = None
        copied_head = solution.copyRandomList(head)
        self.assertIsNone(copied_head)

    def test_single_node(self):
        # Input: head = [[1,null]]
        # Output: [[1,null]]
        solution = Solution()
        head = self.create_linked_list_with_random([[1, None]])
        copied_head = solution.copyRandomList(head)
        result = self.linked_list_to_list(copied_head)
        target = [[1, None]]
        self.assertEqual(result, target)
        
        # Verify deep copy
        self.assertIsNot(head, copied_head)