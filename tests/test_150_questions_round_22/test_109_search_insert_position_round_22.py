import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_109_search_insert_position import Solution


class SearchInsertTestCase(unittest.TestCase):

    def test_target_found(self):
        solution = Solution()
        output = solution.searchInsert(nums=[1,3,5,6], target=5)
        self.assertEqual(output, 2)

    def test_insert_middle(self):
        solution = Solution()
        output = solution.searchInsert(nums=[1,3,5,6], target=2)
        self.assertEqual(output, 1)

    def test_insert_end(self):
        solution = Solution()
        output = solution.searchInsert(nums=[1,3,5,6], target=7)
        self.assertEqual(output, 4)