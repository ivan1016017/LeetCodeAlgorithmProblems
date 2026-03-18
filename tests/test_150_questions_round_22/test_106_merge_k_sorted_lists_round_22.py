import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_106_merge_k_sorted_lists import ListNode, Solution


class MergeKSortedListTestCase(unittest.TestCase):
    
    def list_to_array(self, head: Optional[ListNode]) -> List[int]:
        """Helper method to convert linked list to array"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def array_to_list(self, arr: List[int]) -> Optional[ListNode]:
        """Helper method to convert array to linked list"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def test_example_1(self):
        """Test case: lists = [[1,4,5],[1,3,4],[2,6]]"""
        solution = Solution()
        lists = [
            self.array_to_list([1, 4, 5]),
            self.array_to_list([1, 3, 4]),
            self.array_to_list([2, 6])
        ]
        result = solution.mergeKLists(lists)
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(self.list_to_array(result), expected)
    
    def test_example_2(self):
        """Test case: lists = []"""
        solution = Solution()
        lists = []
        result = solution.mergeKLists(lists)
        self.assertIsNone(result)
    
    def test_example_3(self):
        """Test case: lists = [[]]"""
        solution = Solution()
        lists = [None]
        result = solution.mergeKLists(lists)
        self.assertIsNone(result)
    
    def test_single_list(self):
        """Test case: single list"""
        solution = Solution()
        lists = [self.array_to_list([1, 2, 3, 4])]
        result = solution.mergeKLists(lists)
        expected = [1, 2, 3, 4]
        self.assertEqual(self.list_to_array(result), expected)
    
    def test_two_lists(self):
        """Test case: two lists"""
        solution = Solution()
        lists = [
            self.array_to_list([1, 3, 5]),
            self.array_to_list([2, 4, 6])
        ]
        result = solution.mergeKLists(lists)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.list_to_array(result), expected)
    
    def test_lists_with_different_lengths(self):
        """Test case: lists with different lengths"""
        solution = Solution()
        lists = [
            self.array_to_list([1]),
            self.array_to_list([1, 3, 4]),
            self.array_to_list([2, 6])
        ]
        result = solution.mergeKLists(lists)
        expected = [1, 1, 2, 3, 4, 6]
        self.assertEqual(self.list_to_array(result), expected)
    
    def test_lists_with_none_values(self):
        """Test case: lists containing None/empty lists"""
        solution = Solution()
        lists = [
            self.array_to_list([1, 4, 5]),
            None,
            self.array_to_list([2, 6])
        ]
        result = solution.mergeKLists(lists)
        expected = [1, 2, 4, 5, 6]
        self.assertEqual(self.list_to_array(result), expected)


if __name__ == '__main__':
    unittest.main()